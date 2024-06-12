FROM odoo:14

USER odoo

WORKDIR /mnt/extra-addons

COPY ./ /mnt/extra-addons/custom_materials

USER root
