from user_management.models.user import User


class Advertiser(User):
    class Meta:
        verbose_name = 'تبلیغ کننده'
        verbose_name_plural = 'تبلیغ کنندگان'
