This file is a reference page for the [README](README.md) file. 

Sample Policy Rego

```
package policy

import future.keywords.every
import future.keywords.in

api_svn := "0.10.0"
framework_svn := "0.1.0"

fragments := [
    {
        "iss": "<DID for issuer>",
        "feed": "<feed endpoint>",
        "minimum_svn": "<semantic versioning>",
        "includes": [<one or more of "containers"|"fragments"|"env_rules"|"namespace">]
    }
]

containers := [
    {
        "command": ["<command>", "<arg0>", "<arg1>", /*...*/],
        "allow_stdio_access": true,
        "signals": [/*...*/],
        "env_rules": [
            {
                "pattern": "<pattern>",
                "strategy": "<string|re2>",
                "required": <true|false>
            },
            /*...*/
        ],
        "layers": [
            "<dm-verity hash>",
            /*...*/
        ],
        "mounts": [
            {
                "destination": "<path>",
                "options": ["<option0>", "<option1>", /*...*/],
                "source": "<source regex>",
                "type": "<mount type>"
            },
            /*...*/
        ],
        "allow_elevated": <true|false>,
        "working_dir": "<path>",
        "exec_processes": [
            {
                "command": ["<command>", "<arg0>", "<arg1>", /*...*/],
                "signals": [/*...*/]
            },
            /*...*/
        ],
    }
]

allow_properties_access := false
allow_dump_stacks := false
allow_runtime_logging := false
allow_environment_variable_dropping := true
allow_unencrypted_scratch := false



mount_device := data.framework.mount_device
unmount_device := data.framework.unmount_device
mount_overlay := data.framework.mount_overlay
unmount_overlay := data.framework.unmount_overlay
create_container := data.framework.create_container
exec_in_container := data.framework.exec_in_container
exec_external := data.framework.exec_external
shutdown_container := data.framework.shutdown_container
signal_container_process := data.framework.signal_container_process
plan9_mount := data.framework.plan9_mount
plan9_unmount := data.framework.plan9_unmount
get_properties := data.framework.get_properties
dump_stacks := data.framework.dump_stacks
runtime_logging := data.framework.runtime_logging
load_fragment := data.framework.load_fragment
scratch_mount := data.framework.scratch_mount
scratch_unmount := data.framework.scratch_unmount

reason := {"errors": data.framework.errors}

```