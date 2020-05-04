from django.contrib import admin
from .models import Election, Candidate, Voter


class CandidateAdmin(admin.ModelAdmin):
    readonly_fields = ['vote_count']


class VoterAdmin(admin.ModelAdmin):
    readonly_fields = ['voted_for', 'has_voted']


# Register your models here.
admin.site.register(Election)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Voter, VoterAdmin)
