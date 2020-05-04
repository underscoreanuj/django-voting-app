from django.db import models
from encrypted_fields import fields


class Election(models.Model):
    election_id = models.CharField(
        primary_key=True, unique=True, max_length=300)
    election_name = fields.EncryptedCharField(max_length=100)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return '''
        {} :: {}
        '''.format(self.election_name, self.election_id)


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate_id = models.CharField(
        primary_key=True, unique=True, max_length=300)
    candidate_name = fields.EncryptedCharField(max_length=100)
    vote_count = fields.EncryptedBigIntegerField(default=0)

    def __str__(self):
        return '''
        {} : {} :: ({})
        '''.format(self.candidate_name, self.candidate_id, self.election)


class Voter(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    voted_for = models.ForeignKey(
        Candidate, blank=True, null=True, on_delete=models.SET_NULL)
    voter_id = models.CharField(
        primary_key=True, unique=True, max_length=300)
    voter_name = fields.EncryptedCharField(max_length=100)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return '''
        {} : {} :: ({})
        '''.format(self.voter_name, self.voter_id, self.election)
