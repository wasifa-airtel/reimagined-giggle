from django.conf.urls import url
from django.conf.urls import patterns, url
from . import divsion_views
from . import district_views
from . import views
from . import country_view
from . import gender_views
from . import patient_views
from . import degreeHealth_views
from . import year_views
from . import month_views
from . import day_views
from . import degreeGeneral_views
from . import eduboard_views
from . import resultdivision_views
from . import physician_views



urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name="login"),
    url(r'^index/$', views.IndexView.as_view(), name="index"),

    url(r'^division/$', divsion_views.division_list, name='division'),
    url(r'^new_division/$', divsion_views.division_create, name='division_new'),
    url(r'^new_division/division.html/$', divsion_views.division_list, name='division_redirect'),
    url(r'^edit_division/(?P<pk>\d+)/$', divsion_views.division_update, name='division_edit'),
    url(r'^edit_division/(?P<pk>\d+)/division.html/$', divsion_views.division_redirect),
    url(r'^delete_division/(?P<pk>\d+)/$', divsion_views.division_delete, name='division_delete'),
    url(r'^delete_division/(?P<pk>\d+)/division.html/$', divsion_views.division_redirect),
    url(r'view_division/(?P<pk>\d+)/$', divsion_views.division_view, name='division_view'),

    url(r'^district/$', district_views.district_list, name='district'),
    url(r'^new_district/$', district_views.district_create, name='district_new'),
    url(r'^new_district/district.html/$', district_views.district_list, name='district_redirect'),
    url(r'^edit_district/(?P<pk>\d+)/$', district_views.district_update, name='district_edit'),
    url(r'^edit_district/(?P<pk>\d+)/district.html/$', district_views.district_redirect),
    url(r'^delete_district/(?P<pk>\d+)/$', district_views.district_delete, name='district_delete'),
    url(r'^delete_district/(?P<pk>\d+)/district.html/$', district_views.district_redirect),
    url(r'view_district/(?P<pk>\d+)/$', district_views.district_view, name='district_view'),

    url(r'^thana/$', views.thana_list, name='thana'),
    url(r'^new/$', views.thana_create, name='thana_new'),
    url(r'^new/thana.html/', views.thana_list, name='thana_redirect'),
    url(r'^edit/(?P<pk>\d+)/$', views.thana_update, name='thana_edit'),
    url(r'^edit/(?P<pk>\d+)/thana.html/$', views.thana_redirect),
    url(r'^delete/(?P<pk>\d+)/$', views.thana_delete, name='thana_delete'),
    url(r'^delete/(?P<pk>\d+)/thana.html/$', views.thana_redirect),
    url(r'^view/(?P<pk>\d+)/$', views.thana_view, name='thana_view'),

    url(r'^country/$',country_view.country_list,name='country'),
    url(r'^new_country/$',country_view.country_create,name='country_new'),
    url(r'^new_country/country.html/$',country_view.country_list,name='country_redirect'),
    url(r'^edit_country/(?P<pk>\d+)/$',country_view.country_update,name='country_edit'),
    url(r'^edit_country/(?P<pk>\d+)/country.html/$',country_view.country_redirect),
    url(r'^delete_country/(?P<pk>\d+)/$',country_view.country_delete,name='country_delete'),
    url(r'^delete_country/(?P<pk>\d+)/country.html/$',country_view.country_redirect),
    url(r'^country_view/(?P<pk>\d+)/$',country_view.country_view,name='country_view'),

    url(r'^gender/$',gender_views.gender_list,name='gender'),
    url(r'^new_gender/$',gender_views.gender_create,name='gender_new'),
    url(r'^new_gender/gender.html/$',gender_views.gender_list,name='gender_redirect'),
    url(r'^edit_gender/(?P<pk>\d+)/$',gender_views.gender_update,name='gender_edit'),
    url(r'^edit_gender/(?P<pk>\d+)/gender.html/$',gender_views.gender_redirect),
    url(r'^delete_gender/(?P<pk>\d+)/$',gender_views.gender_delete,name='gender_delete'),
    url(r'^delete_gender/(?P<pk>\d+)/gender.html/$',gender_views.gender_redirect),
    url(r'^gender_view/(?P<pk>\d+)/$',gender_views.gender_view,name='gender_view'),

    url(r'^patient/$',patient_views.patient_list,name='patient'),
    url(r'^new_patient/$',patient_views.patient_create,name='patient_new'),
    url(r'^new_patient/patient.html/$',patient_views.patient_list,name='patient_redirect'),
    url(r'^edit_patient/(?P<pk>\d+)/$',patient_views.patient_update,name='patient_edit'),
    url(r'^edit_patient/(?P<pk>\d+)/patient.html/$',patient_views.patient_redirect),
    url(r'^delete_patient/(?P<pk>\d+)/$',patient_views.patient_delete,name='patient_delete'),
    url(r'^delete_patient/(?P<pk>\d+)/patient.html/$',patient_views.patient_redirect),
    url(r'^patient_view/(?P<pk>\d+)/$',patient_views.patient_view,name='patient_view'),

    url(r'^degreeHealth/$',degreeHealth_views.degreehealth_list,name='degreehealth'),
    url(r'^new_degreeHealth/$',degreeHealth_views.degreehealth_create,name='degreehealth_new'),
    url(r'^new_degreeHealth/degreeHealth.html/$',degreeHealth_views.degreehealth_list,name='degreehealth_redirect'),
    url(r'^edit_degreeHealth/(?P<pk>\d+)/$',degreeHealth_views.degreehealth_update,name='degreehealth_edit'),
    url(r'^edit_degreeHealth/(?P<pk>\d+)/degreeHealth.html/$',degreeHealth_views.degreehealth_redirect),
    url(r'^delete_degreeHealth/(?P<pk>\d+)/$',degreeHealth_views.degreehealth_delete,name='degreehealth_delete'),
    url(r'^delete_degreeHealth/(?P<pk>\d+)/degreeHealth.html/$',degreeHealth_views.degreehealth_redirect),
    url(r'^degreehealth_view/(?P<pk>\d+)/$',degreeHealth_views.degreehealth_view,name='degreehealth_view'),

    url(r'^year/$',year_views.year_list,name='year'),
    url(r'^new_year/$',year_views.year_create,name='year_new'),
    url(r'^new_year/year.html/$',year_views.year_list,name='year_redirect'),
    url(r'^edit_year/(?P<pk>\d+)/$',year_views.year_update,name='year_edit'),
    url(r'^edit_year/(?P<pk>\d+)/year.html/$',year_views.year_redirect),
    url(r'^delete_year/(?P<pk>\d+)/$',year_views.year_delete,name='year_delete'),
    url(r'^delete_year/(?P<pk>\d+)/year.html/$',year_views.year_redirect),
    url(r'^year_view/(?P<pk>\d+)/$',year_views.year_view,name='year_view'),

    url(r'^month/$',month_views.month_list,name='month'),
    url(r'^new_month/$',month_views.month_create,name='month_new'),
    url(r'^new_month/month.html/$',month_views.month_list,name='month_redirect'),
    url(r'^edit_month/(?P<pk>\d+)/$',month_views.month_update,name='month_edit'),
    url(r'^edit_month/(?P<pk>\d+)/month.html/$',month_views.month_redirect),
    url(r'^delete_month/(?P<pk>\d+)/$',month_views.month_delete,name='month_delete'),
    url(r'^delete_month/(?P<pk>\d+)/month.html/$',month_views.month_redirect),
    url(r'^month_view/(?P<pk>\d+)/$',month_views.month_view,name='month_view'),

    url(r'^day/$',day_views.day_list,name='day'),
    url(r'^new_day/$',day_views.day_create,name='day_new'),
    url(r'^new_day/day.html/$',day_views.day_list,name='day_redirect'),
    url(r'^edit_day/(?P<pk>\d+)/$',day_views.day_update,name='day_edit'),
    url(r'^edit_day/(?P<pk>\d+)/day.html/$',day_views.day_redirect),
    url(r'^delete_day/(?P<pk>\d+)/$',day_views.day_delete,name='day_delete'),
    url(r'^delete_day/(?P<pk>\d+)/day.html/$',day_views.day_redirect),
    url(r'^day_view/(?P<pk>\d+)/$',day_views.day_view,name='day_view'),

    url(r'^degreeGeneral/$',degreeGeneral_views.degreeGeneral_list,name='degreegeneral'),
    url(r'^new_degreeGeneral/$',degreeGeneral_views.degreeGeneral_create,name='degreegeneral_new'),
    url(r'^new_degreeGeneral/degreegeneral.html/$',degreeGeneral_views.degreeGeneral_list,name='degreegeneral_redirect'),
    url(r'^edit_degreeGeneral/(?P<pk>\d+)/$',degreeGeneral_views.degreeGeneral_update,name='degreegeneral_edit'),
    url(r'^edit_degreeGeneral/(?P<pk>\d+)/degreegeneral.html/$',degreeGeneral_views.degreegeneral_redirect),
    url(r'^delete_degreeGeneral/(?P<pk>\d+)/$',degreeGeneral_views.degreeGeneral_delete,name='degreegeneral_delete'),
    url(r'^delete_degreeGeneral/(?P<pk>\d+)/degreegeneral.html/$',degreeGeneral_views.degreegeneral_redirect),
    url(r'^degreegeneral_view/(?P<pk>\d+)/$',degreeGeneral_views.degreegeneral_view,name='degreegeneral_view'),

    url(r'^educationboard/$',eduboard_views.eduboard_list,name='eduboard'),
    url(r'^new_educationboard/$',eduboard_views.eduboard_create,name='eduboard_new'),
    url(r'^new_educationboard/eduboard.html/$',eduboard_views.eduboard_list,name='eduboard_redirect'),
    url(r'^edit_educationboard/(?P<pk>\d+)/$',eduboard_views.eduboard_update,name='eduboard_edit'),
    url(r'^edit_educationboard/(?P<pk>\d+)/eduboard.html/$',eduboard_views.eduboard_redirect),
    url(r'^delete_educationboard/(?P<pk>\d+)/$',eduboard_views.eduboard_delete,name='eduboard_delete'),
    url(r'^delete_educationboard/(?P<pk>\d+)/eduboard.html/$',eduboard_views.eduboard_redirect),
    url(r'^educationboard_view/(?P<pk>\d+)/$',eduboard_views.eduboard_view,name='eduboard_view'),

    url(r'^resdiv/$',resultdivision_views.resultdvision_list,name='resdiv'),
    url(r'^new_resdiv/$',resultdivision_views.resultdivision_create,name='resdiv_new'),
    url(r'^new_resdiv/resdiv.html/$',resultdivision_views.resultdvision_list,name='resdiv_redirect'),
    url(r'^edit_resdiv/(?P<pk>\d+)/$',resultdivision_views.resultdivision_update,name='resdiv_edit'),
    url(r'^edit_resdiv/(?P<pk>\d+)/resdiv.html/$',resultdivision_views.resultdivision_redirect),
    url(r'^delete_resdiv/(?P<pk>\d+)/$',resultdivision_views.resultdivision_delete,name='resdiv_delete'),
    url(r'^delete_resdiv/(?P<pk>\d+)/resdiv.html/$',resultdivision_views.resultdivision_redirect),
    url(r'^resdiv_view/(?P<pk>\d+)/$',resultdivision_views.resultdivision_view,name='resdiv_view'),

    url(r'^physician/$',physician_views. physician_list,name='physician'),
    url(r'^new_physician/$',physician_views. PhysicianCreateView.as_view(),name='physician_new'),
    url(r'^new_physician/physician.html/$',physician_views.physician_list,name='physician_redirect'),
    url(r'^edit_phy/(?P<pk>\d+)/$',physician_views.PhysicianUpdateView.as_view(),name='physician_edit'),
    url(r'^edit_phy/(?P<pk>\d+)/physician.html/$',physician_views.physician_redirect),
    url(r'^delete_physician/(?P<pk>\d+)/$',physician_views.physician_delete,name='physician_delete'),
    url(r'^delete_physician/(?P<pk>\d+)/physician.html/$',physician_views.physician_redirect),
    url(r'^physician_view/(?P<pk>\d+)/$',physician_views.PhysicianView.as_view(),name='physician_view'),

]



