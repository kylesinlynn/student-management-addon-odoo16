from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Char(string='Student ID', readonly=True, copy=False)
    birth_date = fields.Date(string='Birth Date')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    image_1920 = fields.Binary(string='Profile Photo')
    course_ids = fields.Many2many(
        'student.course',
        'student_course_rel',
        'student_id',
        'course_id',
        string='Courses'
    )
    advisor_id = fields.Many2one('res.users', string='Advisor')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('graduated', 'Graduated'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')

    course_count = fields.Integer(string='Course Count', compute='_compute_course_count')

    @api.depends('course_ids')
    def _compute_course_count(self):
        for record in self:
            record.course_count = len(record.course_ids)

    @api.model
    def create(self, vals):
        if not vals.get('student_id'):
            vals['student_id'] = self.env['ir.sequence'].next_by_code('student.student') or 'STU0001'
        return super(Student, self).create(vals)

    @api.constrains('email')
    def _check_email_unique(self):
        for record in self:
            if record.email:
                existing = self.search([
                    ('email', '=', record.email),
                    ('id', '!=', record.id)
                ])
                if existing:
                    raise ValidationError("Email already exists!")

    @api.constrains('birth_date')
    def _check_birth_date(self):
        for record in self:
            if record.birth_date and record.birth_date >= date.today():
                raise ValidationError("Birth date must be in the past!")

    def action_confirm(self):
        self.state = 'confirmed'

    def action_graduate(self):
        self.state = 'graduated'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_reset_to_draft(self):
        self.state = 'draft'

    def action_view_courses(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Student Courses',
            'res_model': 'student.course',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', self.course_ids.ids)],
            'context': {'default_student_ids': [(6, 0, [self.id])]},
        }
