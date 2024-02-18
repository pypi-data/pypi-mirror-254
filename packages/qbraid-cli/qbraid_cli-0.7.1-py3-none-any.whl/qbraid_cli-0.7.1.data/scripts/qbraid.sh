#!/usr/bin/env bash

############################### QBRAID CLI ###############################
##########################################################################
# Command Line Interface for interacting with the qBraid Lab platform

# (C) Copyright 2024 qBraid Development Team

############################### PRESCRIPT ################################
#-------------------------------------------------------------------------
# Global variables

# Styling
NC="\033[0m" # No Color
PURPLE="\033[0;35m"
LIGHTPURPLE="\033[1;35m"
RED="\033[0;31m"
GREEN="\033[0;32m"

# Environment directory paths
USER_ENVS=${QBRAID_USR_ENVS:-"/home/jovyan/.qbraid/environments"}
OPT_ENVS=${QBRAID_SYS_ENVS:-"/opt/.qbraid/environments"}

# Arg parse
NUMARGS=$#
FLAGHELP=false

if [ "${NUMARGS}" -gt 0 ]; then
    lastArg=$(echo "${@: -1}")
    if [ "${lastArg}" = "-h" ] || [ "${lastArg}" = "--help" ] || [ "${lastArg}" = "help" ]; then
        FLAGHELP=true
    fi
fi


#-------------------------------------------------------------------------
# Environment slug to display name associative array

declare -A jovyan_envs
declare -A opt_envs=(
    ["qbraid_000000"]="default"
)
declare -A installed_envs

#-------------------------------------------------------------------------
# Environment display name to slug associative array 

is_valid_slug() {
    local slug=$1
    local len_slug=${#slug}

    # Check if the slug is of valid length
    if [ "$len_slug" -gt 20 ]; then
        return 1
    fi

    # Extract the alphanumeric part and check its length
    local alphanumeric_part=${slug: -6}
    if ! [[ $alphanumeric_part =~ ^[a-zA-Z0-9]{6}$ ]]; then
        return 1
    fi

    # Check if it contains an underscore before the alphanumeric part
    if [ "${slug: -7:-6}" != "_" ]; then
        return 1
    fi

    # Check if the remaining part of the slug contains only lowercase letters, numbers, and underscores
    local remaining_part=${slug:0:-7}
    if ! [[ $remaining_part =~ ^[a-z0-9_]*$ ]]; then
        return 1
    fi

    return 0 # Valid slug
}

process_installed_envs() {
    local directory=$1
    local -n envs=$2

    for entry in "$directory"/*
    do
        dir_name=$(basename "$entry")

        if is_valid_slug "$dir_name"; then
            slug_prefix=${dir_name:0:-7}

            if [[ -v envs[$dir_name] ]]; then
                env_name=${envs[$dir_name]}
            elif [[ -v installed_envs[$slug_prefix] ]]; then
                env_name=${dir_name}
                envs[$dir_name]=$env_name
            else
                env_name=${slug_prefix}
                envs[$dir_name]=$env_name
            fi

            # Check if env_name already exists in installed_envs
            if [[ -v installed_envs[$env_name] ]]; then
                # Use dir_name as the new environment name
                env_name=$dir_name
            fi

            if [ "$env_name" != "" ]; then
                installed_envs[$env_name]=$dir_name
            fi
        fi
    done
}

process_installed_envs "$OPT_ENVS" opt_envs
process_installed_envs "$USER_ENVS" jovyan_envs



#-------------------------------------------------------------------------
# Helper functions 

# echos yes if should print help else no
help_command() {
    if [ "${FLAGHELP}" = true ] && [ "${1}" = "${NUMARGS}" ]; then
        echo "yes"
    fi
}

find_match() {
    local -n envs=$1
    local target=$2
    local path=$3

    # Check if the item is a key
    if [[ -n "${envs["$target"]+isset}" ]]; then
        echo "$path/$target"
        return 0
    fi

    # Check if the item is a value
    for key in "${!envs[@]}"; do
        if [ "$target" = "${envs[$key]}" ]; then
            echo "$path/$key"
            return 0
        fi
    done

    # backwards compatibility
    if [ "$target" = "amazon_braket" ]; then
        slug="aws_braket_kwx6dl"
        echo "$path/$slug"
        return 0
    fi

    return 1
}

which_env() {
    local result

    result=$(find_match jovyan_envs "$1" "${USER_ENVS}")
    if [ $? -eq 0 ]; then
        echo "$result"
        return
    fi

    result=$(find_match opt_envs "$1" "${OPT_ENVS}")
    if [ $? -eq 0 ]; then
        echo "$result"
        return
    fi

    echo "None"
}

is_installed() {
    local result
    
    # use which_env helper with dummy argument for path
    result=$(find_match installed_envs "$1" "dummy_path")
    if [ $? -eq 0 ]; then
        echo true
    else
        echo false
    fi
}


print_env_entry() {
    env_name=$1
    count=$((25-${#env_name}))
    env_path=$(which_env "${env_name}")
    proxydir=$(which_jobs "${env_name}")
    python_path="${env_path}/pyenv/bin/python"
    active_indicator=""

    if [ "${python_path}" = "$(which python)" ]; then
        active_indicator="* "
        count=$((count-2))
    fi

    if [ "${proxydir}" = "None" ]; then
        echo -e "${env_name}$(spaces ${count})${active_indicator}      ${env_path}"
    else
        proxyfile="${proxydir}/proxy"
        enabled=$(head -n 1 "${proxyfile}" | grep true)
        if [[ $enabled == *"true"* ]]; then
            echo -e "${env_name}$(spaces ${count})${active_indicator}${GREEN}jobs${NC}  ${env_path}"
        else
            echo -e "${env_name}$(spaces ${count})${active_indicator}${RED}jobs${NC}  ${env_path}"
        fi
    fi
}


has_package() {

    local env_path=$(which_env "${1}")
    local venv_path="${env_path}/pyenv"
    local cfg_file="$venv_path/pyvenv.cfg"
    local package_name=$2


    # Check if the virtual environment directory exists
    if [ ! -d "$venv_path" ]; then
        echo "Error: Virtual environment path '$venv_path' does not exist." >&2
        return 1
    fi

    # Check if the pyvenv.cfg file exists
    if [ ! -f "$cfg_file" ]; then
        echo "Error: Configuration file '$cfg_file' does not exist." >&2
        return 1
    fi

    # Get original value of include-system-site-packages
    local original_value=$(grep "^include-system-site-packages = " "$cfg_file" | cut -d ' ' -f 3)

    # Set include-system-site-packages to false
    sed -i "s/^include-system-site-packages = .*/include-system-site-packages = false/" "$cfg_file"

    # Activate the virtual environment and check if the package is installed
    source "$venv_path/bin/activate"
    if pip freeze | grep -i "^$package_name==" >/dev/null; then
        local package_installed=true
    else
        local package_installed=false
    fi
    deactivate

    # Set include-system-site-packages back to original value
    sed -i "s/^include-system-site-packages = .*/include-system-site-packages = $original_value/" "$cfg_file"

    # Return boolean of whether package exists in venv
    echo $package_installed
}

install_complete() {
    local result

    result=$(find_match opt_envs "$1" "${OPT_ENVS}")
    if [ $? -eq 0 ]; then
        echo true
        return 0
    fi
    
    env_path=$(which_env "${1}")
    if [ -z "$env_path" ]; then
        >&2 echo -e "${RED}ERROR: Failed to determine the environment path for ${NC}'${1}'"
        exit 1
    fi
    
    status_txt="${env_path}/install_status.txt"
    if [[ ! -f "$status_txt" ]]; then
        echo true
    #     >&2 echo -e "${RED}ERROR: File not found${NC} \"$status_txt\""
    #     exit 1
    # fi
    
    elif grep -q "complete:1" "$status_txt"; then
        echo true
    else
        echo false
    fi
    
    return 0
}

which_jobs() {
    local env_path proxy_dir

    env_path=$(which_env "${1}")
    proxy_dir="${env_path}/qbraid"
    # Temporarily only support AWS jobs
    if [[ ! -f "${proxy_dir}/proxy" ]]; then
        echo "None"
    elif [ -d "${proxy_dir}/botocore" ]; then
        echo "${proxy_dir}"
    else
        echo "None"
    fi
}

jobs_enabled() {

    local env_name=$1
    local proxydir=$(which_jobs "${env_name}")
    
    if [ "${proxydir}" = "None" ]; then
        echo false
        return 0
    fi
    
    local proxyfile="${proxydir}/proxy"
    if [[ ! -f "$proxyfile" ]]; then
        >&2 echo -e "${RED}ERROR: File not found${NC} \"$proxyfile\""
        exit 1
    fi

    local enabled=$(head -n 1 "${proxyfile}" | grep true)
    if [[ $enabled == *"true"* ]]; then
        echo true
    else
        echo false
    fi

    return 0
}

swap_files() {

    if [[ ! -f "$1" ]]; then
        >&2 echo -e "${RED}ERROR: File not found${NC} \"$1\""
        exit 1
    fi
    
    local TMPFILE=tmp.$$
    sudo mv "$1" $TMPFILE && sudo mv "$2" "$1" && sudo mv $TMPFILE "$2"
}

qbraid_verify() {

    local qbraidrc="$HOME/.qbraid/qbraidrc"

    if [[ ! -f "$qbraidrc" ]]; then
        >&2 echo -e "${RED}ERROR: File not found${NC} \"$qbraidrc\""
        exit 1
    fi
}

aws_configure() {

    local conf=$HOME/.aws/config
    local cred=$HOME/.aws/credentials

    if [[ ! -f "$conf" ]] || ! grep -q region "$conf"; then
        aws configure set region us-east-1
    fi

    if ! grep -q output "$conf"; then
        aws configure set output json
    fi

    if [[ ! -f "$cred" ]] || ! grep -q aws_access_key_id "$cred"; then
        aws configure set aws_access_key_id MYACCESSKEY  # dummy variable
    fi

    if ! grep -q aws_secret_access_key "$cred"; then
        aws configure set aws_secret_access_key MYSECRETKEY  # dummy variable
    fi
    
}

ibm_save_account() {
    # get jobs command (enable/disable)
    command=$1

    local qiskit_dir="$HOME/.qiskit"
    local qiskit_ibm="$qiskit_dir/qiskit-ibm.json"
    local qiskit_rc="$qiskit_dir/qiskitrc"
    local qbraid_rc="$HOME/.qbraid/qbraidrc"

    write_qiskit_ibm_json() {
        local url="$1"
        local file_path="$qiskit_ibm"

        local content="{
    \"default-ibm-quantum\": {
        \"channel\": \"ibm_quantum\",
        \"token\": \"QISKIT_IBM_TOKEN\",
        \"url\": \"${url}\"
    }
}"

        echo "$content" > "$file_path"
    }

    write_qiskitrc() {
        local url="$1"
        local file_path="$qiskit_rc"

        local content="[ibmq]
token = QISKIT_IBM_TOKEN
url = ${url}
verify = True
default_provider = ibm-q/open/main"

        echo "$content" > "$file_path"
    }

    if [ -f "$qbraid_rc" ]; then
        qbraid_url=$(grep -E '^url\s*=' "$qbraid_rc" | sed -E 's/^url\s*=\s*(.*)/\1/' | sed 's/[[:space:]]*$//')
    else
        qbraid_url="https://api.qbraid.com/api"
    fi

    ibm_url="https://auth.quantum-computing.ibm.com/api"
    qbraid_ibm_url="${qbraid_url}/ibm-routes?route="

    if [ "$command" = "enable" ]; then
        mkdir -p "$qiskit_dir"

        if [ ! -f "$qiskit_rc" ]; then
            write_qiskitrc "$qbraid_ibm_url"
        else
            sed -i "s|${ibm_url}|${qbraid_ibm_url}|g" "$qiskit_rc"
        fi

        if [ ! -f "$qiskit_ibm" ]; then
            write_qiskit_ibm_json "$qbraid_ibm_url"
        else
            sed -i "s|${ibm_url}|${qbraid_ibm_url}|g" "$qiskit_ibm"
        fi
    else
        if [ -f "$qiskit_rc" ]; then
            sed -i "s|${qbraid_ibm_url}|${ibm_url}|g" "$qiskit_rc"
        fi

        if [ -f "$qiskit_ibm" ]; then
            sed -i "s|${qbraid_ibm_url}|${ibm_url}|g" "$qiskit_ibm"
        fi
    fi
}

get_provider() {
    aws=false
    ibm=false
    proxydir=${1}
    command=${2}

    # Temporarily disabling IBM quantum jobs
    # if [ -d "${proxydir}/requests" ]; then
    #     ibm=true
    #     ibm_save_account "$command"
    # fi
    
    if [ -d "${proxydir}/botocore" ]; then
        aws=true
        if [ "${command}" = "enable" ]; then
            aws_configure
        fi
    fi
                    
    if [ "$aws" = true ] && [ "$ibm" = true ]; then
        echo "AWS + IBM"
    elif [ "$aws" = true ]; then
        echo "AWS"
    elif [ "$ibm" = true ]; then
        echo "IBM"
    else
        echo ""
    fi  
}

toggle_proxy() {

    local proxydir=$1
    local action=$2
    local proxyfile="${proxydir}/proxy"
    
    if [[ ! -f "$proxyfile" ]]; then
        >&2 echo -e "${RED}ERROR: File not found${NC} \"$proxyfile\""
        exit 1
    
    else
        for pkgdir in `find "$proxydir" -type d`; do
            # Temporarily skip swap for IBM jobs
            if [ "$pkgdir" != "$proxydir" ] && [[ ! "$pkgdir" =~ "requests" ]]; then
                swapfile="${pkgdir}/swap"
                src=$(grep "src = " "$swapfile" | cut -b 7-)
                dst=$(grep "dst = " "$swapfile" | cut -b 7-)
                
                # Check if both src and dst files exist
                if [ ! -f "$src" ] || [ ! -f "$dst" ]; then
                    echo -e "${RED}ERROR: Failed to enable qBraid Quantum Jobs.${NC}"
                    echo ""
                    echo "File '$src' or '$dst' does not exist." >&2
                    exit 1
                fi

                swap_files "$src" "$dst"
            fi
        done
        
        if [ "${action}" = "enable" ]; then
            sudo sed -i 's/false/true/' "$proxyfile"
        elif [ "${action}" = "disable" ]; then
            sudo sed -i 's/true/false/' "$proxyfile"
        else
            enabled=$(head -n 1 "${proxyfile}" | grep true)
            if [[ $enabled == *"true"* ]]; then
                sudo sed -i 's/true/false/' "$proxyfile"
            else
                sudo sed -i 's/false/true/' "$proxyfile"
            fi
        fi
    fi

}

get_python_version() {
    local venv_path=$1

    # Check if the virtual environment directory exists
    if [ ! -d "$venv_path" ]; then
        echo "Error: Virtual environment path '$venv_path' does not exist." >&2
        return 1
    fi

    # Activate the virtual environment
    source "$venv_path/bin/activate"

    # Get Python major and minor version
    python_version=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')

    # Deactivate the virtual environment
    deactivate

    echo $python_version
}

update_swapfile_python() {
    local qbraid_dir=$1
    local src_version=$2
    local target_version=$3

    # Check if the qbraid directory exists
    if [ ! -d "$qbraid_dir" ]; then
        echo "Error: Directory '$qbraid_dir' does not exist." >&2
        return 1
    fi

    # Find and process each swap.txt file
    find "$qbraid_dir" -type f -name "swap" | while read swapfile; do
        # Check if the file contains the source version
        if grep -q "$src_version" "$swapfile"; then
            # Replace the source version with the target version
            sed -i "s/$src_version/$target_version/g" "$swapfile"
        fi
    done
}


############################### ENVS GROUP ###############################
#-------------------------------------------------------------------------
# Help functions

# qbraid envs -h
help_envs() {
    echo ""
    echo "Group"
    echo "    qbraid envs         : Manage qBraid environments."
    echo ""
    echo "Commands"
    echo "    list                : Get list of installed qBraid environments."
    echo "    activate            : Activate qBraid environment."
    echo "    uninstall           : Uninstall qBraid environment."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help          : Show this help message and exit."
    echo ""
}

# qbraid envs list -h
help_envs_list() {
    echo ""
    echo "Command"
    echo "    qbraid envs list    : Get list of installed qBraid environments."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help          : Show this help message and exit."
    echo ""
}

# qbraids envs activate -h
help_envs_activate() {
    echo ""
    echo "Command"
    echo "    qbraid envs activate [env_name]    : Activate qBraid environment."
    echo ""
    echo "Positional Arguments"
    echo -e "    env_name                           : Name of environment. Values from: \`qbraid envs list\`."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                         : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    qbraid envs activate amazon_braket"
    echo "    qbraid envs activate qbraid_sdk"
    echo ""
}

# qbraids envs uninstall -h
help_envs_uninstall() {
    echo ""
    echo "Command"
    echo "    qbraid envs uninstall [env_name]    : Uninstall qBraid environment."
    echo ""
    echo "Positional Arguments"
    echo -e "    env_name                            : Name of environment. Values from: \`qbraid envs list\`."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                          : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    qbraid envs uninstall amazon_braket"
    echo "    qbraid envs uninstall qbraid_sdk"
    echo ""
}

# qbraids envs sys-packages -h
help_envs_sys_packages() {
    echo ""
    echo "Help command not available"
    echo ""
}


#-------------------------------------------------------------------------
# qbraid envs commands
spaces() {
        for (( a=0; a<(( $1 )); a++ )); do echo -n " "; done
}

envs() {
    
    argDepth=2
    
    # qbraid envs -h
    if [ "$(help_command "${argDepth}")" = "yes" ]; then
        help_envs
    
    # qbraid envs
    elif [ -z "${1}" ]; then
        echo -e "${RED}ERROR: Invalid command${NC}"
        echo ""
        echo -e "Use \`qbraid envs -h\` to see available commands"
        exit 1
    
    # qbraid envs list
    elif [ "${1}" = "list" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_envs_list
        else
            echo -e "# installed environments:"
            echo "#"

            # Print the "default" environment first
            print_env_entry "default"

            # Next, loop through opt_envs
            for key in "${!opt_envs[@]}"; do
                env_name=${opt_envs[$key]}
                if [ "${env_name}" = "default" ]; then
                    continue
                fi
                if [ "$(is_installed "${key}")" = true ]; then
                    print_env_entry "${env_name}"
                fi
            done

            # Finally, loop through installed_envs (done in 2 steps for ordering list by opt then user envs)
            for key in "${!installed_envs[@]}"; do
                # Skip the opt_envs and "default" environment since they've already been displayed
                if [[ -v opt_envs[${installed_envs[$key]}] ]] || [ "${key}" = "default" ]; then
                    continue
                fi
                print_env_entry "${key}"
            done
            echo ""
        fi

    # qbraid envs activate
    elif [ "${1}" = "activate" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_envs_activate
        else
            env_path=$(which_env "${2}")
            if [ "${env_path}" != "None" ] && [ "$(is_installed "${2}")" = true ]; then
                if [ "${2}" = "qsharp" ]; then
                    echo -e "The ${LIGHTPURPLE}${2}${NC} environment uses the base \`/opt/conda/bin/python\` interpreter, so is already \"active\", by default."
                elif [ "$(install_complete "${2}")" != true ]; then
                    echo -e "${RED}ERROR: Resource busy ${NC}${2}"
                    echo ""
                    echo -e "Cannot activate while installing. Please wait for environment to finish installing, and try again."
                    exit 1
                else
                    echo -e "${PURPLE}Activating ${LIGHTPURPLE}${2}${PURPLE} environment... ${NC}"
                    echo -e ""
                    echo -e "${PURPLE}Once active, use ${NC}\`deactivate\`${PURPLE} to deactivate the environment.${NC}"
                    if [ "$(jobs_enabled "${2}")" = true ]; then
                        echo ""
                        echo -e "${RED}WARNING: Quantum jobs enabled for ${NC}${2}. ${RED}Executing ${NC}\`pip install\`${RED} commands with quantum jobs enabled can break environment's qBraid configuration. It is recommended to disable quantum jobs before proceeding${NC}."
                    fi
                    echo "${env_path}/pyenv/bin"
                fi
            else
                echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                echo ""
                echo -e "Environment ${PURPLE}${2}${NC} is not installed. Use \`qbraid envs list\` to see installed environments."
                exit 1
            fi
        fi

    # qbraid envs uninstall
    elif [ "${1}" = "uninstall" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_envs_uninstall
        elif [ "${2}" = "default" ] || [ "${2}" = "qsharp" ] || [ "${2}" = "intel" ]; then
            echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
            echo ""
            echo -e "Environment ${2} comes pre-installed with qBraid Lab, so cannot be uninstalled."
        else
            envdir=$(which_env "${2}")
            if [ "${envdir}" != "None" ] && [ "$(is_installed "${2}")" = true ]; then
                tmpdir="${HOME}/.qbraid/environments/tmp_${2}"
                mv "${envdir}" "${tmpdir}"
                rm -rf "${tmpdir}" &
                echo -e "Uninstalling ${2}..."
                echo ""
                echo -e "${PURPLE}Use ${NC}\`qbraid envs list\` ${PURPLE}to see updated list of installed environments.${NC}"
                echo -e "${PURPLE}Click refresh button in ENVS sidebar to sync lab environment manager frontend.${NC}"
            else
                echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                echo ""
                echo -e "Environment ${PURPLE}${2}${NC} is not installed. Use \`qbraid envs list\` to see installed environments."
                exit 1
            fi
        fi
        
    # qbraid envs sys-packages
    elif [ "${1}" = "sys-packages" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_envs_sys_packages
        elif [ "${2}" = "default" ] || [ "${2}" = "qsharp" ] || [ "${2}" = "intel" ]; then
            echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
            echo ""
            echo -e "Environment ${2} comes pre-installed with qBraid Lab, so value cannot be set."
        else
            envdir=$(which_env "${2}")
            if [ "${envdir}" != "None" ] && [ "$(is_installed "${2}")" = true ]; then
                cfg_path="${envdir}/pyenv/pyvenv.cfg"
                if [[ ! -f "$cfg_path" ]]; then
                    echo "File $cfg_path not found"
                    return 1
                fi

                local from_str
                local to_str

                if [[ "${3}" == "true" ]]; then
                    from_str="include-system-site-packages = false"
                    to_str="include-system-site-packages = true"
                else
                    from_str="include-system-site-packages = true"
                    to_str="include-system-site-packages = false"
                fi
                
                sed -i "s/$from_str/$to_str/g" "$cfg_path"
            else
                echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                echo ""
                echo -e "Environment ${PURPLE}${2}${NC} is not installed. Use \`qbraid envs list\` to see installed environments."
                exit 1
            fi
        fi
                
    else
        echo -e "${RED}ERROR: Invalid argument ${NC}${1}"
        echo ""
        echo -e "Use \`qbraid envs -h\` to see available commands"
        exit 1
    fi
}


############################### KERNELS GROUP ############################
#-------------------------------------------------------------------------
# Help functions

# qbraid kernels -h
help_kernels() {
    echo ""
    echo "Group"
    echo "    qbraid kernels      : Manage qBraid kernel specifications."
    echo ""
    echo "Commands"
    echo "    list                : List installed qBraid kernel specifications."
    echo "    install             : Install a kernel specification directory."
    echo "    uninstall           : Alias for remove"
    echo "    remove              : Remove one or more qBraid kernelspecs by name."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help          : Show this help message and exit."
    echo ""
}

#-------------------------------------------------------------------------
# qbraid kernels commands

kernels() {
    argDepth=2
    
    # qbraid kernels -h
    if [ "$(help_command "${argDepth}")" = "yes" ]; then
        help_kernels

    # qbraid kernels
    elif [ -z "${1}" ]; then
        echo -e "${RED}ERROR: Invalid command ${NC}"
        echo ""
        echo -e "Use \`qbraid kernels -h\` to see available commands"
        exit 1
    else
        jupyter kernelspec "${@:1}"
    fi
}

############################### JOBS GROUP ###############################
#-------------------------------------------------------------------------
# Help functions

# qbraid jobs -h
help_jobs() {
    echo ""
    echo "Group"
    echo "    qbraid jobs         : Manage qBraid Quantum Jobs."
    echo ""
    echo "Commands"
    echo "    list                : Get list of qBraid Quantum Jobs."
    echo "    add                 : Add qBraid Quantum Jobs to environment."
    echo "    enable              : Enable qBraid Quantum Jobs."
    echo "    disable             : Disable qBraid Quantum Jobs."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help          : Show this help message and exit."
    echo ""
}

# qbraid jobs list -h
help_jobs_list() {
    echo ""
    echo "Command"
    echo "    qbraid jobs list    : Get list of qBraid Quantum Jobs."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help          : Show this help message and exit."
    echo ""
}

# qbraid jobs add -h
help_jobs_add() {
    echo ""
    echo "Command"
    echo "    qbraid jobs add [env_name]    : Add qBraid AWS Quantum Jobs support for environment."
    echo ""
    echo "Positional Arguments"
    echo -e "    env_name                      : Name of environment. Values from: \`qbraid envs list\`."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                    : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    qbraid jobs add custom_braket_env"
    echo ""
}

# qbraids jobs enable -h
help_jobs_enable() {
    echo ""
    echo "Command"
    echo "    qbraid jobs enable [env_name]    : Disable qBraid Quantum Jobs."
    echo ""
    echo "Positional Arguments"
    echo -e "    env_name                         : Name of environment. Values from: \`qbraid envs list\`."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                       : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    qbraid jobs enable amazon_braket"
    echo "    qbraid jobs enable qbraid_sdk"
    echo ""
}

# qbraid jobs disable -h
help_jobs_disable() {
    echo ""
    echo "Command"
    echo "    qbraid jobs disable [env_name]    : Disable qBraid Quantum Jobs."
    echo ""
    echo "Positional Arguments"
    echo -e "    env_name                          : Name of environment. Values from: \`qbraid envs list\`."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                        : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    qbraid jobs disable amazon_braket"
    echo "    qbraid jobs disable qbraid_sdk"
    echo ""
}

#-------------------------------------------------------------------------
# qbraid jobs commands

jobs() {

    argDepth=2
    
    # qbraid jobs -h
    if [ "$(help_command "${argDepth}")" = "yes" ]; then
        help_jobs

    # qbraid jobs
    elif [ -z "${1}" ]; then
        echo -e "${RED}ERROR: Invalid command ${NC}"
        echo ""
        echo -e "Use \`qbraid jobs -h\` to see available commands"
        exit 1
    
    # qbraid jobs list
    elif [ "${1}" = "list" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_jobs_list
        fi
 
    # qbraid jobs add
    elif [ "${1}" = "add" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_jobs_add
        else 
            if [ "$(is_installed "${2}")" = true ]; then
                proxydir=$(which_jobs "${2}")
                if [ ${proxydir} = "None" ]; then
                    package="amazon-braket-sdk"
                    if [ "$(has_package "${2}" "${package}")" = true ]; then
                        env_default=$(which_env "default")
                        enabled=$(head -n 1 "${env_default}/qbraid/proxy" | grep true)
                        if [[ $enabled == *"true"* ]]; then
                            echo -e "${RED}ERROR: Resources unavailable${NC}"
                            echo ""
                            echo -e "Quantum jobs must be disabled in the ${PURPLE}default${NC} environment to complete operation." 
                            echo -e "Run ${NC} \`qbraid jobs disable default\`, and try again."
                            exit 1
                        else
                            envdir=$(which_env "${2}")
                            proxy_dir="${envdir}/qbraid"
                            mkdir ${proxy_dir}
                            slug=${envdir##*/}
                            braketswap="${envdir}/qbraid/amazon-braket-sdk/swap"
                            botoswap="${envdir}/qbraid/botocore/swap"
                            cp -r ${env_default}/qbraid/* ${proxy_dir}
                            sed -i "s_opt_home/jovyan_" "${braketswap}"
                            sed -i "s/qbraid_000000/${slug}/" "${braketswap}"
                            sed -i "s_opt_home/jovyan_" "${botoswap}"
                            sed -i "s/qbraid_000000/${slug}/" "${botoswap}"
                            
                            default_python=$(get_python_version "${env_default}/pyenv")
                            target_python=$(get_python_version "${envdir}/pyenv")
                            update_swapfile_python "${envdir}/qbraid" "${default_python}" "${target_python}"
                            
                            echo -e "${PURPLE}Success! Your ${LIGHTPURPLE}${2}${NC}${PURPLE} environment now supports qBraid (AWS) Quantum Jobs${NC}."
                            echo ""
                            echo -e "${PURPLE}To enable Quantum Jobs, run:${NC} \`qbraid jobs enable ${2}\`"
                        fi
                    else
                        echo -e "${RED}ERROR: Package(s) not found: ${NC}${package}"
                        echo ""
                        echo -e "Environment ${PURPLE}${2}${NC} must have '${package}' installed before qBraid Quantum Jobs can be added."
                        exit 1
                    fi
                else
                    echo -e "${PURPLE}Your ${LIGHTPURPLE}${2}${NC}${PURPLE} environment already supports qBraid (AWS) Quantum Jobs${NC}!"
                fi
            else
                echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                echo ""
                echo -e "Environment ${PURPLE}${2}${NC} is not installed. Use \`qbraid envs list\` to see installed environments."
                exit 1
            fi
        fi
    
    # qbraid jobs enable
    elif [ "${1}" = "enable" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_jobs_enable
        else
            if [ "$(is_installed "${2}")" = true ]; then
                if [ "$(install_complete "${2}")" != true ]; then
                    echo -e "${RED}ERROR: Resource busy ${NC}${2}"
                    echo ""
                    echo -e "Cannot enable quantum jobs while installing. Please wait for environment to finish installing, and try again."
                    exit 1
                fi
                proxydir=$(which_jobs "${2}")
                if [ ! ${proxydir} = "None" ]; then
                    qbraid_verify
                    provider=$(get_provider "${proxydir}" "${1}")
                    proxyfile="$proxydir/proxy"
                    enabled=$(head -n 1 "${proxyfile}" | grep true)
                    if [[ $enabled == *"true"* ]]; then
                        echo -e "${PURPLE}You have already enabled qBraid Quantum Jobs in the ${2} environment.${NC}"
                    else
                        toggle_proxy "${proxydir}" "${1}"
                        enabled=$(head -n 1 "${proxyfile}" | grep true)
                        if [[ $enabled == *"true"* ]]; then
                            echo -e "${PURPLE}Successfully enabled qBraid Quantum Jobs in the ${LIGHTPURPLE}${2}${NC}${PURPLE} environment.${NC}"
                            echo -e "${PURPLE}Every ${LIGHTPURPLE}${provider}${NC}${PURPLE} job you run will now be submitted through the qBraid API, so no access keys/tokens are necessary. ${NC}"
                            echo ""
                            echo -e "${PURPLE}To disable, run:${NC} \`qbraid jobs disable ${2}\`"
                        else
                            echo -e "${RED}ERROR: Failed to enable qBraid Quantum Jobs.${NC}"
                            exit 1
                        fi
                    fi
                else
                    echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                    echo ""
                    echo -e "qBraid Quantum Jobs not configured for ${PURPLE}${2}${NC} environment."
                    exit 1
                fi
            else
                echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                echo ""
                echo -e "Environment ${PURPLE}${2}${NC} is not installed. Use \`qbraid envs list\` to see installed environments."
                exit 1
            fi
        fi
        
    # qbraid jobs disable
    elif [ "${1}" = "disable" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_jobs_disable
        else
            if [ "$(is_installed "${2}")" = true ]; then
                proxydir=$(which_jobs "${2}")
                if [ ! ${proxydir} = "None" ]; then
                    provider=$(get_provider "${proxydir}" "${1}")
                    proxyfile="$proxydir/proxy"
                    enabled=$(head -n 1 "${proxyfile}" | grep false)
                    if [[ $enabled == *"false"* ]]; then
                        echo -e "${PURPLE} You have already disabled qBraid Quantum Jobs in the ${LIGHTPURPLE}${2}${NC}${PURPLE} environment.${NC}"
                    else
                        toggle_proxy "${proxydir}" "${1}"
                        executed=$(head -n 1 "${proxyfile}" | grep false)
                        if [[ $executed == *"false"* ]]; then  
                            echo -e "${PURPLE}Disable successful. You are now submitting quantum jobs with your own $provider credentials.${NC}"
                            echo ""
                            echo -e "${PURPLE}To re-enable, run:${NC} \`qbraid jobs enable ${2}\`"
                        else
                            echo -e "${RED}ERROR: Failed to disable qBraid Quantum Jobs. ${NC}"
                            exit 1
                        fi
                    fi
                else
                    echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                    echo ""
                    echo -e "qBraid Quantum Jobs not configured for ${PURPLE}${2}${NC} environment."
                    exit 1
                fi
            else
                echo -e "${RED}ERROR: Invalid argument ${NC}${2}"
                echo ""
                echo -e "Environment ${PURPLE}${2}${NC} is not installed. Use \`qbraid envs list\` to see installed environments."
                exit 1
            fi
        fi
    
    # qbraid jobs get-credits
    elif [ "${1}" = "get-credits" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_jobs_credits
        else
            creditsFile="$HOME/.qbraid/qBraidCredits";
            if [ ! -f "${creditsFile}" ]; then
                echo -e "${RED}ERROR: Number of qBraid credits could not be determined. ${NC}"
                exit 1
            else
                # Read number from the file
                credits=$(head -n 1 "${creditsFile}")

                # Round the number to two decimal places
                rounded_credits=$(printf "%.2f\n" "$credits")

                echo -e "${PURPLE}You have ${NC}$rounded_credits${PURPLE} remaining qBraid credits.${NC}"
            fi
        fi
    
    else 
        echo -e "${RED}ERROR: Invalid argument ${NC}${1}"
        echo ""
        echo -e "Use \`qbraid jobs -h\` to see available commands"
        exit 1
    
    fi
}

############################### DEVICES GROUP ###############################
#-------------------------------------------------------------------------
# Help functions

# qbraid devices -h
help_devices() {
    echo ""
    echo "Group"
    echo "    qbraid devices         : Manage qBraid Quantum Devices."
    echo ""
    echo "Commands"
    echo "    list                   : Get list of qBraid Quantum Devices."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help             : Show this help message and exit."
    echo ""
}

# qbraid devices list -h
help_devices_list() {
    echo ""
    echo "Command"
    echo "    qbraid devices list    : Get list of qBraid Quantum Jobs."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help             : Show this help message and exit."
    echo ""
}

#-------------------------------------------------------------------------
# qbraid devices commands

devices() {

    argDepth=2
    
    # qbraid jobs -h
    if [ "$(help_command "${argDepth}")" = "yes" ]; then
        help_devices

    # qbraid jobs
    elif [ -z "${1}" ]; then
        echo -e "${RED}ERROR: Invalid command ${NC}"
        echo ""
        echo -e "Use \`qbraid devices -h\` to see available commands"
        exit 1
    
    # qbraid devices list
    elif [ "${1}" = "list" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_devices_list
        fi
    else
        echo -e "${RED}ERROR: Invalid argument ${NC}${1}"
        echo ""
        echo -e "Use \`qbraid devices -h\` to see available commands"
        exit 1
    fi
}

############################### CLI ENTRYPOINT ###########################
#-------------------------------------------------------------------------
# Help functions

# qbraid -h
help() {
    echo ""
    echo "Group"
    echo "    qbraid"
    echo ""
    echo "Commands"
    echo "    credits              : Get number of qBraid credits remaining."
    echo "    configure            : Update or add qbraidrc config values."
    echo "    configure set        : Update single qbraidrc config value."
    echo ""
    echo "Subgroups"
    echo "    envs                 : Manage qBraid environments."
    echo "    kernels              : Manage qBraid kernels."
    echo "    jobs                 : Manage qBraid Quantum Jobs."
    echo "    devices              : Manage qBraid Quantum Devices."
    echo ""
    echo "Arguments"
    echo "    -V, --version    : Show version and exit"
    echo ""
    echo "Global Arguments"
    echo "    -h, --help       : Show this help message and exit."
    echo ""
    echo "Reference Docs: https://docs.qbraid.com/projects/cli/en/latest/cli/qbraid.html"
}

# qbraid configure -h
help_configure() {
    echo ""
    echo "Command"
    echo "    qbraid configure                 : Update or add qbraidrc config values."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                       : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    $ qbraid configure"
    echo "    email [None]: contact@qbraid.com"
    echo "    api-key [None]: 1234567890"
    echo ""
}

# qbraid configure set -h
help_configure_set() {
    echo ""
    echo "Command"
    echo "    qbraid configure set [key] [value]                 : Update qbraidrc config value."
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help                       : Show this help message and exit."
    echo ""
    echo "Examples"
    echo "    $ qbraid configure set email contact@qbraid.com"
    echo ""
}

# qbraid credits -h
help_credits() {
    echo ""
    echo "Command"
    echo "    qbraid credits    : Get number of qBraid credits remaining." 
    echo ""
    echo "Optional Arguments"
    echo "    -h, --help        : Show this help message and exit."
    echo ""
}

#-------------------------------------------------------------------------
# command parser / dispatch

qbraid() {

    argDepth=1
    
    # qbraid -h
    if [ "$(help_command "${argDepth}")" = "yes" ]; then
        help
    
    # qbraid
    elif [ -z "${1}" ]; then
        echo -e "---------------------------------"
        echo -e " * ${PURPLE}Welcome to the qBraid CLI!${NC} * "
        echo -e "---------------------------------"
        echo -e ""
        echo -e "        ____            _     _  " 
        echo -e "   __ _| __ ) _ __ __ _(_) __| | "
        echo -e "  / _  |  _ \|  __/ _  | |/ _  | " 
        echo -e " | (_| | |_) | | | (_| | | (_| | " 
        echo -e "  \__  |____/|_|  \__ _|_|\__ _| "
        echo -e "     |_|                         "
        echo -e ""
        echo -e ""
        echo -e "- Use \`qbraid -h\` to see available commands."
        echo -e ""
        echo -e "- Use \`qbraid --version\` to display the current version."
        echo -e ""
        echo -e "Reference Docs: https://docs.qbraid.com/projects/cli/en/latest/cli/qbraid.html"

    # qbraid configure
    elif [ "${1}" = "configure" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_configure
        elif [ "${2}" = "set" ]; then
            ((argDepth++))
            if [ "$(help_command "${argDepth}")" = "yes" ]; then
                help_configure_set
            else
                echo -e "${RED}ERROR: Invalid command ${NC}"
                echo ""
                echo -e "Use \`qbraid configure set -h\` to see available commands"
                exit 1
            fi
        else
            echo -e "${RED}ERROR: Invalid command ${NC}"
            echo ""
            echo -e "Use \`qbraid -h\` to see available commands"
            exit 1
        fi

    # qbraid credits
    elif [ "${1}" = "credits" ]; then
        ((argDepth++))
        if [ "$(help_command "${argDepth}")" = "yes" ]; then
            help_credits
        fi

    # qbraid envs
    elif [ "${1}" = "envs" ]; then
        envs "${@:2}"

    # qbraid kernels
    elif [ "${1}" = "kernels" ]; then
        kernels "${@:2}"
    
    # qbraid jobs
    elif [ "${1}" = "jobs" ]; then
        jobs "${@:2}"
    
    # qbraid devices
    elif [ "${1}" = "devices" ]; then
        devices "${@:2}"

    else
        echo -e "${RED}ERROR: Invalid argument ${NC}${1}"
        echo ""
        echo -e "Use \`qbraid -h\` to see available commands"
        exit 1
    fi

}


#-------------------------------------------------------------------------
# run command

qbraid "$@"
