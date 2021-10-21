# --fake migration 

- Suppose your mother has created 10 samosas for 10 people. (**Django created 10 tables**)
- And you ate 5 of them. (**you deleted 5 of them**)

- You knew your mistake but told mother to make 5 remaining samosa.(**python manage.py migrate**)
- But mother's reply was "I have already created 10". (**No change detected**)
- Now you are screwed cus guest started to arrive and mother can't be blamed cus you ate 5 samosas.(**It is not Django's concern what you do to your database after he created it.**)

## ways to cleans your sins

### 1. Make 5 samosa by your own:-

It is very time consuming process and you may create mistake while you are making them. 

<span style = "color:red">Guests are waiting!!</span>

#### 2. Buy 5 new samosas and replace them.

1. Clear the remaining of samosas from the plate. (**Delete migrations folder. If the table you want to create is related to app1 than only delete app1/migration folder do not touch others** .<span style = "color:red">If the table you deleted have foreign key related conflicts then delete their migration folder too to avoid chaose.</span>)
2. Clear table where you ate the samosas. (**Go to mysql -->Database-->Delete app1 table in django_migration**)
3. Take out samosa's from the Zomato bags. (**python manage.py makemigrations app1**)
4. Put new samosa's in the plate with existing samosas.(**python manage.py migrate app1 --fake** )

5. As you are putting 5 new samosas with old 5 samosas --fake your impressions. (**only tables which are missing will be created other will be faked**)

> # “If at first you don't succeed, remove all evidence you ever tried. ”    

**Reference**:-

Django Documentation :- [click me](https://docs.djangoproject.com/en/3.2/topics/migrations/)   <span style= 'color:green'>**note:- If you don't want loss your hairs ,read links listed below first. **</span> 

Stake overflow 1 :- [click me](https://stackoverflow.com/questions/42695629/fake-initial-vs-fake-in-django-migration)

Stake overflow 2:- [click me](https://stackoverflow.com/questions/33259477/how-to-recreate-a-deleted-table-with-django-migrations)

**created_by = "Mohamamd_Sharique"**

