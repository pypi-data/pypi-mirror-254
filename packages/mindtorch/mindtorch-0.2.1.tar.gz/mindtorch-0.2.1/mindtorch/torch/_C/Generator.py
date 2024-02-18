from mindspore.common.api import jit_class

@jit_class
class Generator():
    def get_state(self):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")

    def initial_seed(self):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")

    def manual_seed(self, seed):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")

    def seed(self):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")

    def set_state(self, new_state):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")

    def __init__(self, device='cpu'):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")

    @staticmethod
    def __new__(cls, *args, **kwargs):
        raise NotImplementedError("`Generator` is not currently supported, please delete it, and you can learn about "
                                  "the impact of modifications through https://www.mindspore.cn/docs/en/r2.1/"
                                  "migration_guide/typical_api_comparision.html#seed-generator")
