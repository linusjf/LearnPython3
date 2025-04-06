#!/usr/bin/env bash
#
# Bash library for dependency checking

set -o errexit
set -o nounset
set -o pipefail

function require() {
  if ! command -v "$1" > /dev/null 2>&1; then
    printf "Error: Required command not found: %s\n" "$1" >&2
    exit 127
  fi
}

function require_file() {
  if [[ ! -f "$1" ]]; then
    printf "Error: Required file not found: %s\n" "$1" >&2
    exit 127
  fi
}

function require_dir() {
  if [[ ! -d "$1" ]]; then
    printf "Error: Required directory not found: %s\n" "$1" >&2
    exit 127
  fi
}

function source_relative() {
  local script_path
  script_path="$(dirname "$(realpath -s "${BASH_SOURCE[1]}")")/$1"
  require_file "$script_path"
  # shellcheck disable=SC1090
  source "$script_path"
}
