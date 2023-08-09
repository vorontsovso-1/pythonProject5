from django.db import models
from django.contrib import admin

class Advertisement(models.Model):
    title=models.CharField(
        max_length=100,
        verbose_name='Название',


    )

    description=models.TextField(
        verbose_name='Описание',
    )
    price=models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2
    )

    auction=models.BooleanField(
        verbose_name='Торг',
        default=False
    )

    created_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"

    )
    updated_at=models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата редактирования'
    )

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.created_at.date() == timezone.now().date():
            created_time= self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='дата редактирования')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')

    class Admin:
        list_display = ["id", "title"]

    def __str__(self):
        return "%s    %s"%(self.id,self.title)

    class Meta:
        db_table='advertisement'
