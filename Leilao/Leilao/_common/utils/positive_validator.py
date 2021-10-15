def validate_positive(value):
    if value <= 0:
        raise ValidationError(
             _('%(value)s is not a positive number'),
            params={'value': value},
        )