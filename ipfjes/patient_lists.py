"""
Defining Opal PatientLists
"""
from opal import core
from opal.models import Episode

from ipfjes import models


class AllPatientsList(core.patient_lists.PatientList):
    display_name = 'All Patients'
    template_name = "patient_lists/ipfjes_list.html"

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment
    ]

    def get_queryset(self, **kwargs):
        return Episode.objects.all()


class ParticipantsToCallList(core.patient_lists.PatientList):
    display_name = 'Participants to call'
    slug = "interviews"
    template_name = "patient_lists/ipfjes_list.html"

    schema = [
        models.Demographics,
        models.GeneralNotes,
        core.patient_lists.Column(
            name="actions",
            title="Actions",
            template_path="interview_actions.html"
            )
        ]

    def get_queryset(self, **kwargs):
        return Episode.objects.filter(
            tagging__value="needs_interview", tagging__archived=False
        )


class OccupationalHistoriesIssuesList(core.patient_lists.PatientList):
    display_name = 'Occupational Histories Issues List'
    slug = "occupational_histories_issues"
    template_name = "patient_lists/ipfjes_list.html"

    schema = [
        models.Demographics,
        models.Diagnosis,
        core.patient_lists.Column(
            name="actions",
            title="Actions",
            template_path="issue_actions.html"
        )
    ]

    def get_queryset(self, **kwargs):
        """
        Episodes that have occupationaly histories where there is
        a soc job but no soc code
        """
        occ_histories = models.OccupationalHistory.objects.filter(
            soc_code=None
        )
        occ_histories = [i for i in occ_histories if i.soc_job]

        return Episode.objects.filter(
            patient__occupationalhistory__in=occ_histories
        )
