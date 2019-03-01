#!/usr/bin/env python3

from ansible.module_utils.basic import AnsibleModule
import wget

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            path=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['path'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
