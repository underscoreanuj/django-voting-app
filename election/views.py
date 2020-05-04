from .models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

# Create your views here.


class index(TemplateView):
    def post(self, request):
        voter_id = request.POST.get('voter_id')
        voter_count = Voter.objects.filter(voter_id=voter_id).count()

        if voter_count == 0:
            return render(request, 'error.html', context={'error_item': "Voter ID"})

        voter = Voter.objects.get(voter_id=voter_id)
        election = voter.election
        candidates = election.candidate_set.all()

        context = {
            'voter_id': voter_id,
            'election': election,
            'candidates': candidates
        }

        if voter.has_voted or election.is_complete:
            voted_for = voter.voted_for
            context = {
                'voter_id': voter_id,
                'election': election,
                'candidates': candidates,
                'voted_for': voted_for
            }

            return render(request, 'result.html', context=context)

        return render(request, 'election.html', context=context)

    def get(self, request):
        return render(request, 'voter_id.html')


class vote(TemplateView):
    def post(self, request):
        candidate_id = request.POST.get('candidate_id')
        print(request.POST)
        candidate = Candidate.objects.get(candidate_id=candidate_id)

        if candidate is not None:
            voter_id = request.POST.get('voter_id')
            voter = Voter.objects.get(voter_id=voter_id)
            candidate.vote_count = candidate.vote_count + 1
            candidate.save()
            voter.has_voted = True
            voter.voted_for = candidate
            voter.save()
        else:
            return render(request, 'error.html', context={'error_item': "Candidate"})

        return HttpResponseRedirect('/election')
