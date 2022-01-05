### To have two primary key

```python
class Hop(models.Model):
    migration = models.ForeignKey('Migration')
    host = models.ForeignKey(User, related_name='host_set')

    class Meta:
        unique_together = (("migration", "host"),)
```

This kind of table is known as composite tables.

