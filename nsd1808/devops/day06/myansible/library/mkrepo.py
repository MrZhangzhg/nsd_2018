#!/usr/bin/env python3

import wget
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mudi=dict(required=True, type='str')
        )
    )
    wget.download(module.params['yuan'], module.params['mudi'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
