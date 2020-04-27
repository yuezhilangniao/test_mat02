from celerytapp.models import User,FreeTime
# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_mat02.settings")# project_name 项目名称
# django.setup()


class InserTime:

    def insert(self,id):
        #id = self.id
        FreeTime.objects.create(who_id=id, fweek=1, fhour=1, fstate=1)

        # for w in range(1, 8):
        #     for h in range(24):
        #         FreeTime.objects.create(
        #             who_id=id,
        #             fweek=w,
        #             fhour=h,
        #             fstate=1
        #         )


if __name__ == '__main__':
    a = InserTime()
    a.insert(1)
