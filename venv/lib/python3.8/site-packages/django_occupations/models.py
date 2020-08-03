"""
Database models for django_occupations.
"""
from django.db import models
from model_utils.models import TimeStampedModel


class ONetAlternateTitle(TimeStampedModel):
    """
    O*Net-SOC Alternate Titles

    From https://www.onetcenter.org/dictionary/24.3/excel/alternate_titles.html
        "...alternate, or 'lay', occupational titles for the O*NET-SOC 
        classification system. The file was developed to improve keyword 
        searches in several Department of Labor internet applications 
        (i.e., Career InfoNet, O*NET OnLine, and O*NET Code Connector).
        The file contains occupational titles from existing occupational 
        classification systems, as well as from other diverse sources. When 
        a title contains acronyms, abbreviations, or jargon, the 'Short Title' 
        column contains the brief version of the full title."

    Note: O*Net also publishes a "source" for the alternate title, but that 
    is not yet being stored here.

    .. no_pii:
    """

    alternate_title = models.CharField(max_length=250)
    short_title = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=150)
    onet_soc_code = models.CharField(max_length=10, null=True)
    onet_soc_occupation = models.ManyToManyField('ONetOccupation')
    soc_occupation = models.ForeignKey('SOCDetailedOccupation', null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<ONetAlternateTitle, ID: {self.id}, Alternate Title: {self.alternate_title}, Title: {self.title}, O*Net-SOC Code: {self.onet_soc_code}>"



class ONetOccupation(TimeStampedModel):
    """
    O*Net-SOC Occupations

    From https://www.onetcenter.org/dl_files/Taxonomy2010_Summary.pdf
        In the O*NET-SOC taxonomy, an occupation that is directly adopted 
        from the SOC system is assigned the six-digit SOC code, along with 
        a .00 extension. If directly adopted from the SOC, the SOC title 
        and definition are also used. Hereafter, these are referred to as 
        SOC-level occupations.
        If the O*NET-SOC occupation is more detailed than the original SOC 
        detailed occupation, it is assigned the six-digit SOC code from 
        which it originated, along with a two-digit extension starting with 
        .01, then .02, .03 and so on, depending on the number of detailed 
        O*NET-SOC occupations linked to the particular SOC detailed 
        occupation.
        For example, Nuclear Technicians is a SOC detailed occupation to 
        which two detailed O*NET-SOC occupations are linked. See the 
        occupational codes and titles for this example below.
            19-4051.00 Nuclear Technicians (SOC-level)
            19-4051.01 Nuclear Equipment Operation Technicians (detailed 
                       O*NET-SOC occupation)
            19-4051.02 Nuclear Monitoring Technicians (detailed O*NET-SOC 
                       occupation) 

    .. no_pii:
    """
    
    onet_soc_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    soc_occupation = models.ForeignKey('SOCDetailedOccupation', null=True,
                                   on_delete=models.SET_NULL)

    def get_description():
        """
        TODO: Return local description if it's available, or the SOC description as a backup, or empty if neither is available
        """
        return

    def is_catchall():
        """
        TODO: Returns True if the SOC code ends in a 9 or have "All other" at the end of the description
        """
        return



class SOCDetailedOccupation(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    soc_code = models.CharField(max_length=10, null=True)
    broad_occupation = models.ForeignKey('SOCBroadOccupation', null=True,
                                   on_delete=models.SET_NULL)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<SOCDetailedOccupation, ID: {self.id}, Name: {self.name}>"


class SOCBroadOccupation(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    soc_code = models.CharField(max_length=10, null=True)
    minor_group = models.ForeignKey('SOCMinorGroup', null=True,
                                   on_delete=models.SET_NULL)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<SOCBroadOccupation, ID: {self.id}, Name: {self.name}>"


class SOCMinorGroup(TimeStampedModel):
    """
    SOC Minor Occupational Groups

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    soc_code = models.CharField(max_length=10, null=True)
    major_group = models.ForeignKey('SOCMajorGroup', null=True,
                                   on_delete=models.SET_NULL)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<SOCMinorGroup, ID: {self.id}, Name: {self.name}>"


class SOCMajorGroup(TimeStampedModel):
    """
    SOC Major Occupational Groups

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)
    soc_code = models.CharField(max_length=10, null=True)
    intermediate_aggregation_group = models.ForeignKey('SOCIntermediateAggregationGroup', null=True,
                                   on_delete=models.SET_NULL)
    high_level_aggregation_group = models.ForeignKey('SOCHighLevelAggregationGroup', null=True,
                                   on_delete=models.SET_NULL)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<SOCMajorGroup, ID: {self.id}, Name: {self.name}>"


class SOCIntermediateAggregationGroup(TimeStampedModel):
    """
    BLS recommended intermediate-level aggregations

    Refer to Table 6 on https://www.bls.gov/soc/2018/soc_2018_manual.pdf

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<SOCIntermediateAggregationGroup, ID: {self.id}, Name: {self.name}>"


class SOCHighLevelAggregationGroup(TimeStampedModel):
    """
    BLS recommended high-level aggregations

    Refer to Table 6 on https://www.bls.gov/soc/2018/soc_2018_manual.pdf

    .. no_pii:
    """

    name = models.CharField(max_length=256, unique=True, null=True)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return f"<SOCHighLevelAggregationGroup, ID: {self.id}, Name: {self.name}>"

