from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'student.course'
    _description = 'Course'
    _rec_name = 'name'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    code = fields.Char(string='Course Code', required=True)
    student_ids = fields.Many2many(
        'student.student',
        'student_course_rel',
        'course_id',
        'student_id',
        string='Students'
    )

    student_count = fields.Integer(string='Student Count', compute='_compute_student_count')

    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)

    @api.constrains('code')
    def _check_code_unique(self):
        for record in self:
            if record.code:
                existing = self.search([
                    ('code', '=', record.code),
                    ('id', '!=', record.id)
                ])
                if existing:
                    raise ValidationError("Course code already exists!")

    def action_view_students(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Course Students',
            'res_model': 'student.student',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.student_ids.ids)],
            'context': {'default_course_ids': [(6, 0, [self.id])]},
        }
