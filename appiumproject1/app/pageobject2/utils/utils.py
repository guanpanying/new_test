import faker as Faker


class Utils:
    @classmethod
    def get_name(self):
        return Faker('zh_CN').name()

    @classmethod
    def get_phonenum(self):
        pass