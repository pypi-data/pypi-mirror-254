# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import _, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class CustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if "outsource_work_outstanding_count" in counters:
            values["outsource_work_outstanding_count"] = (
                request.env["outsource_work_outstanding"].search_count([])
                if request.env["outsource_work_outstanding"].check_access_rights(
                    "read", raise_exception=False
                )
                else 0
            )
        if "outsource_work_count" in counters:
            values["outsource_work_count"] = (
                request.env["outsource_work"].search_count([])
                if request.env["outsource_work"].check_access_rights(
                    "read", raise_exception=False
                )
                else 0
            )
        return values

    def _outsource_work_outstanding_get_page_view_values(
        self, outsource_work_outstanding, access_token, **kwargs
    ):
        values = {
            "page_name": "outsource-work-outstandings",
            "outsource_work_outstanding": outsource_work_outstanding,
        }
        return self._get_page_view_values(
            outsource_work_outstanding,
            access_token,
            values,
            "my_outsource_work_outstandings_history",
            False,
            **kwargs
        )

    @http.route(
        [
            "/my/outsource-work-outstandings",
            "/my/outsource-work-outstandings/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_outsource_work_outstandings(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        values = self._prepare_portal_layout_values()
        Outstanding = request.env["outsource_work_outstanding"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("# Outstanding"), "order": "name"},
        }
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]

        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]

        # outsource work outstanding count
        outsource_work_outstanding_count = Outstanding.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/outsource-work-outstandings",
            url_args={"date_begin": date_begin, "date_end": date_end, "sortby": sortby},
            total=outsource_work_outstanding_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        outsource_work_outstandings = Outstanding.search(
            domain, order=order, limit=self._items_per_page, offset=pager["offset"]
        )
        request.session[
            "my_outsource_work_outstandings_history"
        ] = outsource_work_outstandings.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "outsource_work_outstandings": outsource_work_outstandings,
                "page_name": "outsource-work-outstandings",
                "default_url": "/my/outsource-work-outstandings",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "sortby": sortby,
            }
        )
        return request.render(
            "ssi_outsource_work.portal_my_outsource_work_outstandings", values
        )

    @http.route(
        ["/my/outsource-work-outstanding/<int:outstanding_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_outsource_work_outstanding(
        self, outstanding_id=None, access_token=None, **kw
    ):
        try:
            outsource_work_outstanding_sudo = self._document_check_access(
                "outsource_work_outstanding", outstanding_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._outsource_work_outstanding_get_page_view_values(
            outsource_work_outstanding_sudo, access_token, **kw
        )
        values.update({"access_token": values.get("access_token", access_token)})
        return request.render(
            "ssi_outsource_work.portal_my_outsource_work_outstanding", values
        )

    def _outsource_work_get_page_view_values(
        self, outsource_work, access_token, **kwargs
    ):
        values = {
            "page_name": "outsource-works",
            "outsource_work": outsource_work,
        }
        return self._get_page_view_values(
            outsource_work,
            access_token,
            values,
            "my_outsource_works_history",
            False,
            **kwargs
        )

    @http.route(
        [
            "/my/outsource-works",
            "/my/outsource-works/page/<int:page>",
        ],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_outsource_works(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        values = self._prepare_portal_layout_values()
        OutsourceWork = request.env["outsource_work"]
        domain = []

        searchbar_sortings = {
            "date": {"label": _("Newest"), "order": "create_date desc"},
            "name": {"label": _("# Outsource Work"), "order": "name"},
        }
        if not sortby:
            sortby = "date"
        order = searchbar_sortings[sortby]["order"]

        if date_begin and date_end:
            domain += [
                ("create_date", ">", date_begin),
                ("create_date", "<=", date_end),
            ]

        # outsource work count
        outsource_work_count = OutsourceWork.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/outsource-works",
            url_args={"date_begin": date_begin, "date_end": date_end, "sortby": sortby},
            total=outsource_work_count,
            page=page,
            step=self._items_per_page,
        )

        # content according to pager and archive selected
        outsource_works = OutsourceWork.search(
            domain, order=order, limit=self._items_per_page, offset=pager["offset"]
        )
        request.session["my_outsource_works_history"] = outsource_works.ids[:100]

        values.update(
            {
                "date": date_begin,
                "date_end": date_end,
                "outsource_works": outsource_works,
                "page_name": "outsource-works",
                "default_url": "/my/outsource-works",
                "pager": pager,
                "searchbar_sortings": searchbar_sortings,
                "sortby": sortby,
            }
        )
        return request.render("ssi_outsource_work.portal_my_outsource_works", values)

    @http.route(
        ["/my/outsource-work/<int:outsource_work_id>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_outsource_work(self, outsource_work_id=None, access_token=None, **kw):
        try:
            outsource_work_sudo = self._document_check_access(
                "outsource_work", outsource_work_id, access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/my")

        values = self._outsource_work_get_page_view_values(
            outsource_work_sudo, access_token, **kw
        )
        values.update({"access_token": values.get("access_token", access_token)})
        return request.render("ssi_outsource_work.portal_my_outsource_work", values)
