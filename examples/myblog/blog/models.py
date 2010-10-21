from django.db import models

class BlogPost(models.Model):
    """
    Simple blog post model for demo purposes.
    """
    
    title = models.CharField('Title', max_length=255)
    text = models.TextField('Text')
    
    class Meta:
        verbose_name='Blog post'
        verbose_name_plural='Blog posts'

    def __unicode__(self):        
        return self.title