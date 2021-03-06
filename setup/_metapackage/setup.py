import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-account-invoicing",
    description="Meta package for oca-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-account_invoice_anglo_saxon_no_cogs_deferral',
        'odoo11-addon-account_invoice_blocking',
        'odoo11-addon-account_invoice_check_total',
        'odoo11-addon-account_invoice_fiscal_position_update',
        'odoo11-addon-account_invoice_fixed_discount',
        'odoo11-addon-account_invoice_force_number',
        'odoo11-addon-account_invoice_line_description',
        'odoo11-addon-account_invoice_pricelist',
        'odoo11-addon-account_invoice_refund_link',
        'odoo11-addon-account_invoice_reimbursable',
        'odoo11-addon-account_invoice_supplier_ref_reuse',
        'odoo11-addon-account_invoice_supplier_ref_unique',
        'odoo11-addon-account_invoice_supplier_self_invoice',
        'odoo11-addon-account_invoice_tax_required',
        'odoo11-addon-account_invoice_triple_discount',
        'odoo11-addon-account_invoice_view_payment',
        'odoo11-addon-account_payment_term_extension',
        'odoo11-addon-purchase_stock_picking_return_invoicing',
        'odoo11-addon-sale_timesheet_invoice_description',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
