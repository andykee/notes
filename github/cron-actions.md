# Scheduling GitHub Actions

In workflow YML file:

```yml
on:
  schedule:
    - cron: '*/30 * * * *'
```

Note: GitHub Free plan limits Actions to 2,000 minutes/month
