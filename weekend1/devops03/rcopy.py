"将远程主机本地的文件拷贝到本机的目标位置"
# -*- coding: utf8 -*-

import shutil
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mubiao=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mubiao'])
    module.exit_json(change=True)

if __name__ == '__main__':
    main()

# ansible all -m rcopy
