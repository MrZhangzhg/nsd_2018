from ansible.module_utils.basic import AnsibleModule
import shutil

def main():
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mudi=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mudi'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
