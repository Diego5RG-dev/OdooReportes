# Copilot Instructions for OdooReportes

## Project Overview
OdooReportes is an **Odoo 18 custom module** (`reportearmodulo`) that extends HR expense functionality to generate PDF reports. The module uses Odoo's QWeb report engine to create customized expense reports.

**Key Stack:**
- Odoo 18.0 framework
- PostgreSQL 16 database
- Docker Compose for local development
- Python 3 (Odoo standard)
- XML for views and report definitions
- QWeb templating for PDF generation

## Module Architecture

### File Structure
```
reportearmodulo/
├── __manifest__.py     # Module metadata and dependencies
├── __init__.py         # Module initialization (imports models & controllers)
├── models/models.py    # Data models (currently commented template)
├── controllers/controllers.py  # HTTP routes (currently commented template)
├── views/
│   ├── views.xml       # UI views and report definitions
│   └── templates.xml   # QWeb templates (currently commented)
├── security/ir.model.access.csv  # Row-level access control
└── demo/demo.xml       # Demo data for testing
```

### Core Workflow
1. **Dependency**: Depends on `hr_expense` module (HR expense management)
2. **Report Binding**: `action_expense_report` in `views.xml` binds a PDF report to the `hr.expense` model
3. **Report Type**: Uses `qweb-pdf` for PDF generation (server-side rendering via Jinja2-like QWeb engine)
4. **Data Flow**: HR expense records → QWeb template → PDF output

## Development Patterns & Conventions

### 1. Module Definition (`__manifest__.py`)
- **Always update** `'version'` for releases (semantic versioning)
- **List dependencies** in `'depends'`: `['hr_expense']` means this module extends HR expense
- **Data files** in `'data'` are loaded on module install/upgrade
- Security CSV must be uncommented in data list when ACLs are needed

### 2. Odoo Model Pattern
Models inherit from `models.Model` and are registered with `_name`:
```python
from odoo import models, fields, api

class ReportModule(models.Model):
    _name = 'reportearmodulo.reportearmodulo'  # Database table reference
    _description = 'Report Module'
    
    # Field definitions use Odoo field types
    name = fields.Char()
    value = fields.Integer()
    
    @api.depends('value')  # Computed fields need explicit depends
    def _compute_field(self):
        for record in self:
            record.result = record.value * 2
```

### 3. Report Definition (`views.xml`)
Report records use `ir.actions.report` model:
```xml
<record id="action_expense_report" model="ir.actions.report">
    <field name="name">Reportador</field>           <!-- UI label -->
    <field name="model">hr.expense</field>          <!-- Linked model -->
    <field name="report_type">qweb-pdf</field>      <!-- PDF output format -->
    <field name="binding_model_id" ref="hr_expense.model_hr_expense"/>
    <field name="binding_type">report</field>       <!-- Menu binding type -->
</record>
```

### 4. Security (ACL)
`security/ir.model.access.csv` controls CRUD permissions by role:
- Format: `id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink`
- `base.group_user` = regular authenticated users
- Uncomment in `__manifest__.py` data list to activate

## Docker Development Environment

### Setup & Execution
```bash
# Start services (PostgreSQL + Odoo + PgAdmin)
docker-compose up -d

# Access services
Odoo:     http://localhost:8069
PgAdmin:  http://localhost:5050 (user@example.com / Admin123..)
Database: localhost:5432 (odoo/odoo)

# Stop services
docker-compose down
```

### Module Installation in Odoo UI
1. Navigate to **Apps** menu
2. Search for "reportearmodulo"
3. Click **Install** (loads data files + enables routes)
4. Upgrade with `-u reportearmodulo` if modifying manifest

### Development Workflow
- **Hot reload**: Modify Python/XML files → restart Odoo container: `docker-compose restart odoo`
- **Database changes**: Models require Odoo service restart for field updates
- **Debug prints**: Use `print()` or `_logger.info()` (check Odoo container logs with `docker logs odoo`)

## Key Integration Points

### Extending `hr.expense`
- Inherit from `hr.expense` to add custom fields or methods
- Use `_inherit = 'hr.expense'` pattern (not `_name`)
- Report will automatically include custom fields in context

### QWeb Report Templates (Not Yet Implemented)
When completing template implementation:
- Reference the report in `report_name` as `'module_name.template_id'`
- Access model data via `doc` variable (the hr.expense record)
- Use QWeb directives: `t-if`, `t-foreach`, `t-esc`, `t-format`

## Common Pitfalls & Debug Tips

| Issue | Solution |
|-------|----------|
| Report not appearing in menu | Verify `binding_model_id` ref matches target model; check `binding_type` |
| Model fields not saving | Ensure model is imported in `__init__.py`; restart Odoo container |
| XML syntax errors | Use `docker logs odoo` to see parse errors on startup |
| Permission denied errors | Check ACL CSV is activated in manifest and group_id is correct |

## Testing & Validation
- **Demo data**: Load via `Settings > Modules > Demo Data` after module install
- **Manual testing**: Use Odoo UI to create/modify expense records and trigger report generation
- **Logs**: Monitor with `docker logs -f odoo` (Python errors, API calls)

## References
- Odoo 18 Report Documentation: https://www.odoo.com/documentation/18.0/developer/reference/backend/reports.html
- QWeb Reference: https://www.odoo.com/documentation/18.0/developer/reference/frontend/qweb.html
- Module Development Guide: https://www.odoo.com/documentation/18.0/developer/howtos/backend.html
