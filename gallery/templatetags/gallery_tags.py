import re

from django import template

from photologue.models import PhotoSizeCache


register = template.Library()


@register.tag
def videoembed(parser, token):
    try:
        tag_name, obj, photosize = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            'videoembed tag requires arguments obj and photosize'
        )
    return VideoEmbedNode(obj, photosize)


class VideoEmbedNode(template.Node):

    def __init__(self, obj, photosize):
        self.obj = template.Variable(obj)
        self.photosize = template.Variable(photosize)

    def render(self, context):
        obj = self.obj.resolve(context)
        photosize = self.photosize.resolve(context)
        size = PhotoSizeCache().sizes.get(photosize + '_LAYER')
        result = obj.embed
        result = re.sub(r'width="([\d]*)"', 'width="%s"' % size.width, result)
        result = re.sub(r'height="([\d]*)"', 'height="%s"' % size.height, result)
        return result
