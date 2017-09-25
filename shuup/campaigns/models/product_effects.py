# This file is part of Shuup.
#
# Copyright (c) 2012-2017, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.db import models
from django.utils.translation import ugettext_lazy as _

from shuup.core.models import PolymorphicShuupModel


class ProductDiscountEffect(PolymorphicShuupModel):
    identifier = None
    model = None
    admin_form_class = None

    campaign = models.ForeignKey("CatalogCampaign", related_name='effects', verbose_name=_("campaign"))

    def apply_for_product(self, context, product, price_info):
        """
        Applies the effect for product

        :type context: shuup.core.pricing._context.PricingContextable
        :return: amount of discount to accumulate for the product
        :rtype: Price
        """
        raise NotImplementedError("Not implemented!")
