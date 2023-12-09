from django.db import models

class PhoneNumber(models.Model):
    COUNTRY_CHOICES = [
        ('Cameroon', 'Cameroon'),
        ('Ethiopia', 'Ethiopia'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Uganda', 'Uganda'),
    ]

    CODE_CHOICES = [
    ('+251', '+237'),
    ('+251', '+251'),
    ('+212 ', '+212 '),
    ('+258 ', '+258 '),
    ('+256', '+256 '),
]

    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    state = models.BooleanField()  
    country_code = models.CharField(max_length=5 , choices=CODE_CHOICES)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.country} - {self.country_code} {self.phone_number}"

