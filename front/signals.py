from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from front.models import Repo, Pipeline
from webhooks import repos

@receiver(pre_save, sender=Repo)
def clone_repo_before_save(sender, instance, **kwargs):
    if not instance.id:
        repos.install(instance)

@receiver(post_save, sender=Repo)
def create_default_pipeline(sender, instance, **kwargs):
    try:
        Pipeline.objects.get(repo=instance, name='default')
        pass
    except ObjectDoesNotExist:
        default_pipeline = Pipeline(repo=instance, name='default', branch_pattern='*')
        default_pipeline.save()
    except:
        pass
