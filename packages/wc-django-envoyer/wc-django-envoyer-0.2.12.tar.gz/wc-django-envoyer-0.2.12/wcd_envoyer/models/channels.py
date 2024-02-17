from django.utils.translation import pgettext_lazy
from wcd_notifications.compat import JSONField

from .. import channels
from ..utils import DynamicChoicesField, get_json_encoder
from .utils import DateTimeModel


__all__ = 'ChannelConfig',


class ChannelConfig(DateTimeModel):
    class Meta:
        verbose_name = pgettext_lazy('wcd_envoyer', 'Channel config')
        verbose_name_plural = pgettext_lazy('wcd_envoyer', 'Channel configs')

    channel = DynamicChoicesField(
        pgettext_lazy('wcd_envoyer', 'Channel'),
        max_length=512, unique=True,
        choices=channels.registry.get_choices,
    )
    data = JSONField(
        pgettext_lazy('wcd_envoyer', 'Data'), default=dict,
        blank=True, null=False, encoder=get_json_encoder(),
    )

    def __str__(self) -> str:
        return self.get_channel_display()
