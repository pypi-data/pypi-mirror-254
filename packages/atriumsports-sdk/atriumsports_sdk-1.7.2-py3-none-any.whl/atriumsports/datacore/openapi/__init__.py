# coding: utf-8

# flake8: noqa

"""
DataCore API  - Sport

# Introduction

The DataCore API is a REST based API. This means it makes use of the followng HTTP primitives:
 * GET - To retrieve data
 * POST - To add a record
 * PUT - To update a record
 * DELETE - To delete a record

All data sent and received as well as error messages is in the JSON format.

## Character Sets and Names

All data sent as both body and query parameters should be in the UTF-8 character set. All data returned will also be in UTF-8 strings.

A number of fields (especially names) have both a *local* and *latin* variant. The *local* variant is the string as it would be written in the local language of the organization.  The *latin* variant is the string as it would be written, only using latin characters/alphabet. Character sets like Cyrillic, Chinese are valid for the *local* string but not the *latin* string.  Regardless of the name, all strings should still be sent using UTF-8.

## Partial Responses

By default, the server sends back the full representation of a resource after processing requests. For better performance, you can ask the server to send only the fields you really need and get a partial response instead. This lets your application avoid transferring, parsing and storing un-needed data.

To request a partial response, use the `fields` query parameter to specify the fields you want returned.

    fields=dob,firstName,familyName,organization(id),organizations[name],teams[name,details/metrics/*,tags(id)]

### Syntax

 Character | Meaning
 --------- | -------
 **,**     | Delimits fields. All fields need to be delimited by a **,**.  eg. `fields=firstName,familyName`
 **/**     | Use `a/b` to select a field b that is nested within field a; use `a/b/c` to select a field c nested within b.
 **( )**   | The subselector allows you to specify a set of sub fields of an array or object by placing those fields in the parentheses. For example `competitors(name,address/state)` would return the name fields of the competitors key and the state field of the address key inside the competitors object.  This is also equivalent to `competitors/name,competitors/address/state`.
 **\***   | The wildcard character matches all fields at a level. eg. `*,organization/id` would return all fields, but only the id field of the organization key
 **[]**  | The field selection will generally only refer to the fields being returned in the *data* section on the response, but by giving the name of the resource type and then enclosing the field selection syntax in square brackets you can select which fields display in the *included* section as well. eg `firstName,familyName,organizations[name,id,country]` will display the firstName and familyName from the data element and only the name, id and country from the organizations resources in the include section.

All field references are relative to the `data` element.

If the resourceType and id fields are not displayed inside the data section for a sub-element, then the system will not make them available for [Resource Inclusion](#Resource_Inclusion), regardless of the use of the includes parameter.


## Pagination
When retrieving information using GET methods, the optional `limit` parameter sets the maximum number of rows to return in a response. The maximum is 1000. If this value is empty `limit` defaults to 10.

If more rows are available, the response will include a `next` element (inside the *links* section), which contains a URL for requesting the next page. If this value is not provided, no more rows are available. A `previous` page element is also provided if appropriate.

These URIs can be generated manually by using the `offset` parameter combined with the `limit` parameter. The `offset` parameter will return `limit` rows of data starting at the **offset + 1** row.


## Sorting
Where allowed, a route can have `sortBy` passed with a list of fields to sort by.  For each allowed field a `-` before the field name will denote DESC sort. The default sort is ASCENDING.
The below example will sort by `startTimeUTC` "descending" then `fixtureNumber` "ascending":

?sortBy=-startTimeUTC,fixtureNumber

## Resource Inclusion
When a response is returned it will not automatically include extra data from other resources/models. It will only list the resource type and id. eg.

        "competition" : {
            "resourceType" : "competitions",
            "id" : "009e9276-5c80-11e8-9c2d-fa7ae01bbebc"
        },
If specified in the query string the `include` parameter will expand that resource in the *includes* section of the response. The `include` parameter takes a comma separated list of resourceTypes to be included.

    /v1/sport/org/1/teams/009e9276-5c80-11e8-9c2d-fa7ae01bbebc?include=competitions,leagues

If the resourceType is included in the parameter and that resourceType is available in the response, then response will include an *includes* key.  Inside that *includes* key is a *resources* object.  Inside that object, there are keys for each type of included resourceType.  Inside each resourceType keyed against the id is an object representing that resource.

    {
        "meta": ...
        "links": ...
        "data": ...
        "includes": {
            "resources": {
                "competitions":
                    "009e9276-5c80-11e8-9c2d-fa7ae01bbebc": {
                        ...
                        Competition Resource Details
                        ...        
                    }
                },
                "leagues": {
                    "009e9276-5c80-11e8-9c2d-fa7bc24e4ebc": {
                        ...
                        League Resource Details
                        ...        
                    }
                }
            }
        }
    }

If the resourceType/id block is not available in the response, then the `include` will not link in the requested resource.  eg. an `include=competitions` in a fixtures call will not return anything as the competition resource is not returned in these calls. However, the include functionality also checks the included resources for resourceType/id blocks. This means that you can chain includes to get further along the data model.  For example an `include=competitions,seasons` in a fixtures call will return the competition resource as the competition resourceType/id block is returned in the season resource.

The list of available inclusions are


 code            | Resource 
 -----            | ----- 
 `competitions`|Competitions
 `entities`      | Entities 
 `entityGroups`|Entity Groups
 `fixtures`|Fixtures
 `leagues`       | Leagues 
 `organizations` | Organizations 
 `persons`|Persons
 `sites`|Sites
 `seasons`|Seasons
 `seasonPools`|Pools
 `seasonStages`|Stages
 `seasonRounds`|Rounds
 `venues`|Venues

## External Ids

The API allows certain end-points to be accessed via the externalId as supplied by the user.  

The external parameter when used, lists the Ids that are to be replaced.

    /v1/sport/org/1/competitions/NL?external=competitionId

Below are a list of all the Ids that can be replaced.  These Ids can be replaced in GET, POST, PUT & DELETE calls.
* competitionId
* seasonId
* fixtureId
* siteId
* venueId
* entityGroupId
* entityId
* personId

The allowable format of an externalId is any character except:
* / (forward slash)
* ? (question mark)
* & (ampersand)

## Date formats

The API only accepts dates formatted in the ISO-8601 standard. These dates should be sent with **no** timezone qualifier. The correct timezone will be implied by the context of the call.

**Example:**

 For dates with a time component

     YYYY-MM-DDThh:mm:ss.s eg. 2017-06-29T18:20:00.00

 For dates with no time component

     YYYY-MM-DD eg. 2017-06-29

where  
 YYYY = four-digit year  
 MM = two-digit month (01=January, etc.)  
 DD = two-digit day of month (01 through 31)  
 hh = two digits of hour (00 through 23) (am/pm NOT allowed)   
 mm = two digits of minute (00 through 59)   
 ss = two digits of second (00 through 59)   
 s = one or more digits representing a decimal fraction of a second  

## UUIDs

The majority of objects in the API use a [universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) (uuid) as an identifier.  The uuid is a number, represented as 32 hexadecimal digits. There are a number of different versions of the uuid, but this API uses only uuid version 1.

When a new record (that uses a uuid) is created, this uuid can be generated by the client and included in the POST call.  If left blank, it will be automatically created by the server and return it in the response.

An example uuid is: `206c7392-b05f-11e8-96f8-529269fb1459`

## Images

Some API calls will return image objects for things such as logos or photos.  The url field of the image object contains the url where you will find that image.  This url is for the 'default' version of the image.  There are some query string parameters available to change how the image is returned.

`format`

 By default the image is returned in whatever format it was uploaded in, but by specifying the 'format' parameter you can change this.  Valid options are: `png`, `jpg`, `webp`.

`size`

By default the image is returned as a square of 100x100 pixels.  By specifying the 'size' parameter the image will be returned at a difference size.  The available options are

size parameter | dimensions
 -----            | -----
`100` | 100x100
`200` | 200x200
`400` | 400x400
`800` | 800x800
`1000` | 1000x1000
`RAW` | The original dimensions that the image was uploaded with

Images will not be scaled up. If you ask for an image with `size=400`, but the image is only 200x200 then the image will be returned as 200x200.

All images returned (apart from `size=RAW`) are square. If the original image that is uploaded is not square, then it is padded with a transparent (white for jpg) background.

An example url is: `https://img.dc.atriumsports.com/586aa6b195d243c4ae4154c8a61eda19?size=200&format=webp`

## DataCore Object Model

<a href = "https://yuml.me/diagram/scruffy;dir:LR/class/[Organizations]-<>[Persons],[Organizations]-.-<>[Leagues],[Organizations]-.-<>[Divisions],[Divisions]-.-<>[Conferences],[Organizations]-<>[Competitions],[Organizations]-<>[Entity Groups],[Organizations]-<>[Venues],[Organizations]-<>[Sites],[Organizations]-<>[Entities],[Competitions]-<>[Seasons],[Leagues]-.-<>[Competitions],[Seasons]-<>[Fixtures],[Fixtures]-2<>[~Competitors~],[~Competitors~]-.->[Conferences][Fixtures]-1[Venues],[Entity Groups]-.-<>[Entities],[Sites]-.-<>[Venues],[Fixtures]-<>[Fixture Roster],[Seasons]->[Stages],[Seasons]->[Pools],[Seasons]->[Rounds],[Fixtures]-.->[Stages],[Fixtures]-.->[Pools],[Fixtures]-.->[Rounds],[~Competitors~]<-[Entities],[Fixture Roster]<-[Persons],[Entities]->[Season Roster],[Season Roster]<-[Persons].jpg">
<img src="https://yuml.me/diagram/scruffy;dir:LR/class/[Organizations]-<>[Persons],[Organizations]-.-<>[Leagues],[Organizations]-.-<>[Divisions],[Divisions]-.-<>[Conferences],[Organizations]-<>[Competitions],[Organizations]-<>[Entity Groups],[Organizations]-<>[Venues],[Organizations]-<>[Sites],[Organizations]-<>[Entities],[Competitions]-<>[Seasons],[Leagues]-.-<>[Competitions],[Seasons]-<>[Fixtures],[Fixtures]-2<>[~Competitors~],[~Competitors~]-.->[Conferences][Fixtures]-1[Venues],[Entity Groups]-.-<>[Entities],[Sites]-.-<>[Venues],[Fixtures]-<>[Fixture Roster],[Seasons]->[Stages],[Seasons]->[Pools],[Seasons]->[Rounds],[Fixtures]-.->[Stages],[Fixtures]-.->[Pools],[Fixtures]-.->[Rounds],[~Competitors~]<-[Entities],[Fixture Roster]<-[Persons],[Entities]->[Season Roster],[Season Roster]<-[Persons]"></a>


More detailed information about each component is available in that section of the API documentation.

## Fixture Status Flow

Each fixture can have one of the following status values:
  * **IF_NEEDED** - Only played if needed
  * **BYE** - Entity has no fixture scheduled for this group of fixtures
  * **SCHEDULED** - Yet to be played
  * **PENDING** - Ready to start
  * **WARM_UP** - Players have begun to warm up
  * **IN_PROGRESS** - Currently in play
  * **FINISHED** - Fixture finished but not yet 'official'
  * **CONFIRMED** - Fixture officially completed
  * **POSTPONED** - Will be played at a future time
  * **CANCELLED** - Will not be played
  * **ABANDONED** - Fixture began but had to be stopped
  
<img src="https://yuml.me/diagram/scruffy/activity/(start)-|a|,|a|->(IF_NEEDED)->(SCHEDULED),|a|->(BYE)->(SCHEDULED),|a|->(SCHEDULED)->(PENDING)->(WARM_UP)->(IN_PROGRESS)->(FINISHED)->(CONFIRMED)->(end),(SCHEDULED)->(CANCELLED)->(end),(SCHEDULED)->(ABANDONED)->(end),(SCHEDULED)->(POSTPONED)->(end),(IN_PROGRESS)->(ABANDONED)->(end)" >

## Limits/Throttling

All API requests are limited/throttled to prevent abuse and ensure stability.  There are two types of limiting in place:
 1. Usage Limits/Quota
    As a customer you would have been given a number of API calls that you are allowed to make each month. If you exceed this limit then your request will fail.
 2. Rate Limits
    As part of your plan you will also have limits as to how often you can make particular calls. For example you may only be able to call a particular endpoint once per minute.  If you exceed these limits then your request will fail.

# Authorization

This API uses the OAuth 2.0 protocol to authorize calls. OAuth is an open standard that many companies use to provide secure access to protected resources.

When you created an application in our management systems you would have been provided with an OAuth client ID and secret key.  By using these credentials and other parameters in a [get token](#token) call you will receive back an **access token**. 

This **access token** must then be sent in the `Authorization` header for each subsequent API call.  Access tokens have a finite life and will expire. When the token expires you will need to create a new token to make more API calls.  Creation of tokens is rate-limited, so you should use the existing token as long as possible.

<!-- ReDoc-Inject: <security-definitions> -->
  # noqa: E501
"""

__version__ = "1.7.2"

# import apis into sdk package
from atriumsports.datacore.openapi.api.awards_api import AwardsApi
from atriumsports.datacore.openapi.api.career_statistics_api import CareerStatisticsApi
from atriumsports.datacore.openapi.api.change_log_api import ChangeLogApi
from atriumsports.datacore.openapi.api.competition_external_ids_api import CompetitionExternalIDsApi
from atriumsports.datacore.openapi.api.competition_statistics_api import CompetitionStatisticsApi
from atriumsports.datacore.openapi.api.competitions_api import CompetitionsApi
from atriumsports.datacore.openapi.api.conduct_api import ConductApi
from atriumsports.datacore.openapi.api.conference_external_ids_api import ConferenceExternalIDsApi
from atriumsports.datacore.openapi.api.conferences_divisions_api import ConferencesDivisionsApi
from atriumsports.datacore.openapi.api.division_external_ids_api import DivisionExternalIDsApi
from atriumsports.datacore.openapi.api.download_video_api import DownloadVideoApi
from atriumsports.datacore.openapi.api.entities_api import EntitiesApi
from atriumsports.datacore.openapi.api.entity_external_ids_api import EntityExternalIDsApi
from atriumsports.datacore.openapi.api.entity_fixture_history_api import EntityFixtureHistoryApi
from atriumsports.datacore.openapi.api.entity_fixture_statistics_api import EntityFixtureStatisticsApi
from atriumsports.datacore.openapi.api.entity_group_external_ids_api import EntityGroupExternalIDsApi
from atriumsports.datacore.openapi.api.entity_groups_api import EntityGroupsApi
from atriumsports.datacore.openapi.api.fixture_entities_api import FixtureEntitiesApi
from atriumsports.datacore.openapi.api.fixture_external_ids_api import FixtureExternalIDsApi
from atriumsports.datacore.openapi.api.fixture_live_summary_api import FixtureLiveSummaryApi
from atriumsports.datacore.openapi.api.fixture_persons_api import FixturePersonsApi
from atriumsports.datacore.openapi.api.fixture_playbyplay_api import FixturePLAYBYPLAYApi
from atriumsports.datacore.openapi.api.fixture_profiles_api import FixtureProfilesApi
from atriumsports.datacore.openapi.api.fixture_progressions_api import FixtureProgressionsApi
from atriumsports.datacore.openapi.api.fixture_roster_api import FixtureRosterApi
from atriumsports.datacore.openapi.api.fixtures_api import FixturesApi
from atriumsports.datacore.openapi.api.images_api import ImagesApi
from atriumsports.datacore.openapi.api.leader_criteria_sets_api import LeaderCriteriaSetsApi
from atriumsports.datacore.openapi.api.leader_qualifiers_api import LeaderQualifiersApi
from atriumsports.datacore.openapi.api.league_external_ids_api import LeagueExternalIDsApi
from atriumsports.datacore.openapi.api.leagues_api import LeaguesApi
from atriumsports.datacore.openapi.api.local_video_endpoints_api import LocalVideoEndpointsApi
from atriumsports.datacore.openapi.api.merge_records_api import MergeRecordsApi
from atriumsports.datacore.openapi.api.organizations_api import OrganizationsApi
from atriumsports.datacore.openapi.api.partner_apis_api import PartnerAPIsApi
from atriumsports.datacore.openapi.api.person_external_ids_api import PersonExternalIDsApi
from atriumsports.datacore.openapi.api.person_fixture_history_api import PersonFixtureHistoryApi
from atriumsports.datacore.openapi.api.person_fixture_statistics_api import PersonFixtureStatisticsApi
from atriumsports.datacore.openapi.api.persons_api import PersonsApi
from atriumsports.datacore.openapi.api.rankings_api import RankingsApi
from atriumsports.datacore.openapi.api.roles_api import RolesApi
from atriumsports.datacore.openapi.api.season_entities_api import SeasonEntitiesApi
from atriumsports.datacore.openapi.api.season_entity_base_statistics_api import SeasonEntityBaseStatisticsApi
from atriumsports.datacore.openapi.api.season_entity_placings_api import SeasonEntityPlacingsApi
from atriumsports.datacore.openapi.api.season_external_ids_api import SeasonExternalIDsApi
from atriumsports.datacore.openapi.api.season_leaders_api import SeasonLeadersApi
from atriumsports.datacore.openapi.api.season_person_base_statistics_api import SeasonPersonBaseStatisticsApi
from atriumsports.datacore.openapi.api.season_person_placings_api import SeasonPersonPlacingsApi
from atriumsports.datacore.openapi.api.season_persons_api import SeasonPersonsApi
from atriumsports.datacore.openapi.api.season_roster_api import SeasonRosterApi
from atriumsports.datacore.openapi.api.season_series_api import SeasonSeriesApi
from atriumsports.datacore.openapi.api.season_statistics_api import SeasonStatisticsApi
from atriumsports.datacore.openapi.api.seasons_api import SeasonsApi
from atriumsports.datacore.openapi.api.site_external_ids_api import SiteExternalIDsApi
from atriumsports.datacore.openapi.api.sites_api import SitesApi
from atriumsports.datacore.openapi.api.stages_pools_rounds_api import StagesPoolsRoundsApi
from atriumsports.datacore.openapi.api.standing_adjustments_api import StandingAdjustmentsApi
from atriumsports.datacore.openapi.api.standing_configurations_api import StandingConfigurationsApi
from atriumsports.datacore.openapi.api.standings_api import StandingsApi
from atriumsports.datacore.openapi.api.transfers_api import TransfersApi
from atriumsports.datacore.openapi.api.venue_external_ids_api import VenueExternalIDsApi
from atriumsports.datacore.openapi.api.venues_api import VenuesApi
from atriumsports.datacore.openapi.api.video_stream_inputs_api import VideoStreamInputsApi
from atriumsports.datacore.openapi.api.video_stream_subscriptions_api import VideoStreamSubscriptionsApi
from atriumsports.datacore.openapi.api.video_streams_available_api import VideoStreamsAvailableApi

# import ApiClient
from atriumsports.datacore.openapi.api_client import ApiClient
from atriumsports.datacore.openapi.api_response import ApiResponse
from atriumsports.datacore.openapi.configuration import Configuration
from atriumsports.datacore.openapi.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from atriumsports.datacore.openapi.models.award_post_body import AwardPostBody
from atriumsports.datacore.openapi.models.award_put_body import AwardPutBody
from atriumsports.datacore.openapi.models.awards_model import AwardsModel
from atriumsports.datacore.openapi.models.awards_model_organization import AwardsModelOrganization
from atriumsports.datacore.openapi.models.awards_response import AwardsResponse
from atriumsports.datacore.openapi.models.blank_model_response import BlankModelResponse
from atriumsports.datacore.openapi.models.career_person_season_statistics_model import CareerPersonSeasonStatisticsModel
from atriumsports.datacore.openapi.models.career_person_season_statistics_model_organization import (
    CareerPersonSeasonStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.career_person_season_statistics_response import (
    CareerPersonSeasonStatisticsResponse,
)
from atriumsports.datacore.openapi.models.career_person_statistics_model import CareerPersonStatisticsModel
from atriumsports.datacore.openapi.models.career_person_statistics_model_organization import (
    CareerPersonStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.career_person_statistics_response import CareerPersonStatisticsResponse
from atriumsports.datacore.openapi.models.change_log_model import ChangeLogModel
from atriumsports.datacore.openapi.models.change_log_model_organization import ChangeLogModelOrganization
from atriumsports.datacore.openapi.models.change_log_response import ChangeLogResponse
from atriumsports.datacore.openapi.models.competition_entity_statistics_model import CompetitionEntityStatisticsModel
from atriumsports.datacore.openapi.models.competition_entity_statistics_model_organization import (
    CompetitionEntityStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.competition_entity_statistics_response import (
    CompetitionEntityStatisticsResponse,
)
from atriumsports.datacore.openapi.models.competition_external_ids_model import CompetitionExternalIdsModel
from atriumsports.datacore.openapi.models.competition_external_ids_model_organization import (
    CompetitionExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.competition_external_ids_post_body import CompetitionExternalIdsPostBody
from atriumsports.datacore.openapi.models.competition_external_ids_put_body import CompetitionExternalIdsPutBody
from atriumsports.datacore.openapi.models.competition_external_ids_response import CompetitionExternalIdsResponse
from atriumsports.datacore.openapi.models.competition_historical_name import CompetitionHistoricalName
from atriumsports.datacore.openapi.models.competition_person_statistics_model import CompetitionPersonStatisticsModel
from atriumsports.datacore.openapi.models.competition_person_statistics_model_organization import (
    CompetitionPersonStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.competition_person_statistics_response import (
    CompetitionPersonStatisticsResponse,
)
from atriumsports.datacore.openapi.models.competition_post_body import CompetitionPostBody
from atriumsports.datacore.openapi.models.competition_put_body import CompetitionPutBody
from atriumsports.datacore.openapi.models.competitions_model import CompetitionsModel
from atriumsports.datacore.openapi.models.competitions_model_league import CompetitionsModelLeague
from atriumsports.datacore.openapi.models.competitions_model_organization import CompetitionsModelOrganization
from atriumsports.datacore.openapi.models.competitions_response import CompetitionsResponse
from atriumsports.datacore.openapi.models.competitions_season_status_model import CompetitionsSeasonStatusModel
from atriumsports.datacore.openapi.models.competitions_season_status_model_league import (
    CompetitionsSeasonStatusModelLeague,
)
from atriumsports.datacore.openapi.models.competitions_season_status_model_organization import (
    CompetitionsSeasonStatusModelOrganization,
)
from atriumsports.datacore.openapi.models.competitions_season_status_response import CompetitionsSeasonStatusResponse
from atriumsports.datacore.openapi.models.conduct_model import ConductModel
from atriumsports.datacore.openapi.models.conduct_model_organization import ConductModelOrganization
from atriumsports.datacore.openapi.models.conduct_penalty_result import ConductPenaltyResult
from atriumsports.datacore.openapi.models.conduct_post_body import ConductPostBody
from atriumsports.datacore.openapi.models.conduct_put_body import ConductPutBody
from atriumsports.datacore.openapi.models.conduct_response import ConductResponse
from atriumsports.datacore.openapi.models.conference_external_ids_model import ConferenceExternalIdsModel
from atriumsports.datacore.openapi.models.conference_external_ids_model_organization import (
    ConferenceExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.conference_external_ids_post_body import ConferenceExternalIdsPostBody
from atriumsports.datacore.openapi.models.conference_external_ids_put_body import ConferenceExternalIdsPutBody
from atriumsports.datacore.openapi.models.conference_external_ids_response import ConferenceExternalIdsResponse
from atriumsports.datacore.openapi.models.conference_post_body import ConferencePostBody
from atriumsports.datacore.openapi.models.conference_put_body import ConferencePutBody
from atriumsports.datacore.openapi.models.conferences_model import ConferencesModel
from atriumsports.datacore.openapi.models.conferences_model_organization import ConferencesModelOrganization
from atriumsports.datacore.openapi.models.conferences_response import ConferencesResponse
from atriumsports.datacore.openapi.models.contact_details import ContactDetails
from atriumsports.datacore.openapi.models.division_external_ids_model import DivisionExternalIdsModel
from atriumsports.datacore.openapi.models.division_external_ids_model_organization import (
    DivisionExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.division_external_ids_post_body import DivisionExternalIdsPostBody
from atriumsports.datacore.openapi.models.division_external_ids_put_body import DivisionExternalIdsPutBody
from atriumsports.datacore.openapi.models.division_external_ids_response import DivisionExternalIdsResponse
from atriumsports.datacore.openapi.models.division_post_body import DivisionPostBody
from atriumsports.datacore.openapi.models.division_put_body import DivisionPutBody
from atriumsports.datacore.openapi.models.divisions_model import DivisionsModel
from atriumsports.datacore.openapi.models.divisions_model_organization import DivisionsModelOrganization
from atriumsports.datacore.openapi.models.divisions_response import DivisionsResponse
from atriumsports.datacore.openapi.models.entities_model import EntitiesModel
from atriumsports.datacore.openapi.models.entities_model_entity_group import EntitiesModelEntityGroup
from atriumsports.datacore.openapi.models.entities_model_organization import EntitiesModelOrganization
from atriumsports.datacore.openapi.models.entities_response import EntitiesResponse
from atriumsports.datacore.openapi.models.entity_additional_details import EntityAdditionalDetails
from atriumsports.datacore.openapi.models.entity_address import EntityAddress
from atriumsports.datacore.openapi.models.entity_external_ids_model import EntityExternalIdsModel
from atriumsports.datacore.openapi.models.entity_external_ids_model_organization import (
    EntityExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.entity_external_ids_post_body import EntityExternalIdsPostBody
from atriumsports.datacore.openapi.models.entity_external_ids_put_body import EntityExternalIdsPutBody
from atriumsports.datacore.openapi.models.entity_external_ids_response import EntityExternalIdsResponse
from atriumsports.datacore.openapi.models.entity_group_address import EntityGroupAddress
from atriumsports.datacore.openapi.models.entity_group_external_ids_model import EntityGroupExternalIdsModel
from atriumsports.datacore.openapi.models.entity_group_external_ids_model_organization import (
    EntityGroupExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.entity_group_external_ids_post_body import EntityGroupExternalIdsPostBody
from atriumsports.datacore.openapi.models.entity_group_external_ids_put_body import EntityGroupExternalIdsPutBody
from atriumsports.datacore.openapi.models.entity_group_external_ids_response import EntityGroupExternalIdsResponse
from atriumsports.datacore.openapi.models.entity_group_historical_name import EntityGroupHistoricalName
from atriumsports.datacore.openapi.models.entity_group_post_body import EntityGroupPostBody
from atriumsports.datacore.openapi.models.entity_group_post_body_additional_names import (
    EntityGroupPostBodyAdditionalNames,
)
from atriumsports.datacore.openapi.models.entity_group_post_body_colors import EntityGroupPostBodyColors
from atriumsports.datacore.openapi.models.entity_group_put_body import EntityGroupPutBody
from atriumsports.datacore.openapi.models.entity_groups_model import EntityGroupsModel
from atriumsports.datacore.openapi.models.entity_groups_model_organization import EntityGroupsModelOrganization
from atriumsports.datacore.openapi.models.entity_groups_response import EntityGroupsResponse
from atriumsports.datacore.openapi.models.entity_historical_name import EntityHistoricalName
from atriumsports.datacore.openapi.models.entity_post_body import EntityPostBody
from atriumsports.datacore.openapi.models.entity_post_body_additional_names import EntityPostBodyAdditionalNames
from atriumsports.datacore.openapi.models.entity_post_body_colors import EntityPostBodyColors
from atriumsports.datacore.openapi.models.entity_put_body import EntityPutBody
from atriumsports.datacore.openapi.models.environmental_details import EnvironmentalDetails
from atriumsports.datacore.openapi.models.error_list_model import ErrorListModel
from atriumsports.datacore.openapi.models.error_model import ErrorModel
from atriumsports.datacore.openapi.models.fixture_competitor import FixtureCompetitor
from atriumsports.datacore.openapi.models.fixture_entities_model import FixtureEntitiesModel
from atriumsports.datacore.openapi.models.fixture_entities_model_conference import FixtureEntitiesModelConference
from atriumsports.datacore.openapi.models.fixture_entities_model_division import FixtureEntitiesModelDivision
from atriumsports.datacore.openapi.models.fixture_entities_model_entity import FixtureEntitiesModelEntity
from atriumsports.datacore.openapi.models.fixture_entities_model_organization import FixtureEntitiesModelOrganization
from atriumsports.datacore.openapi.models.fixture_entities_post_body import FixtureEntitiesPostBody
from atriumsports.datacore.openapi.models.fixture_entities_response import FixtureEntitiesResponse
from atriumsports.datacore.openapi.models.fixture_entity_period_statistics_post_body import (
    FixtureEntityPeriodStatisticsPostBody,
)
from atriumsports.datacore.openapi.models.fixture_entity_statistics_model import FixtureEntityStatisticsModel
from atriumsports.datacore.openapi.models.fixture_entity_statistics_model_organization import (
    FixtureEntityStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.fixture_entity_statistics_periods_model import (
    FixtureEntityStatisticsPeriodsModel,
)
from atriumsports.datacore.openapi.models.fixture_entity_statistics_periods_model_organization import (
    FixtureEntityStatisticsPeriodsModelOrganization,
)
from atriumsports.datacore.openapi.models.fixture_entity_statistics_periods_response import (
    FixtureEntityStatisticsPeriodsResponse,
)
from atriumsports.datacore.openapi.models.fixture_entity_statistics_post_body import FixtureEntityStatisticsPostBody
from atriumsports.datacore.openapi.models.fixture_entity_statistics_response import FixtureEntityStatisticsResponse
from atriumsports.datacore.openapi.models.fixture_external_ids_model import FixtureExternalIdsModel
from atriumsports.datacore.openapi.models.fixture_external_ids_model_organization import (
    FixtureExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.fixture_external_ids_post_body import FixtureExternalIdsPostBody
from atriumsports.datacore.openapi.models.fixture_external_ids_put_body import FixtureExternalIdsPutBody
from atriumsports.datacore.openapi.models.fixture_external_ids_response import FixtureExternalIdsResponse
from atriumsports.datacore.openapi.models.fixture_live_summary_model import FixtureLiveSummaryModel
from atriumsports.datacore.openapi.models.fixture_live_summary_response import FixtureLiveSummaryResponse
from atriumsports.datacore.openapi.models.fixture_participant import FixtureParticipant
from atriumsports.datacore.openapi.models.fixture_pbp_event_model import FixturePbpEventModel
from atriumsports.datacore.openapi.models.fixture_pbp_event_model_organization import FixturePbpEventModelOrganization
from atriumsports.datacore.openapi.models.fixture_pbp_event_post_body import FixturePBPEventPostBody
from atriumsports.datacore.openapi.models.fixture_pbp_event_put_body import FixturePBPEventPutBody
from atriumsports.datacore.openapi.models.fixture_pbp_event_response import FixturePbpEventResponse
from atriumsports.datacore.openapi.models.fixture_pbp_model import FixturePbpModel
from atriumsports.datacore.openapi.models.fixture_pbp_model_organization import FixturePbpModelOrganization
from atriumsports.datacore.openapi.models.fixture_pbp_response import FixturePbpResponse
from atriumsports.datacore.openapi.models.fixture_person_statistics_model import FixturePersonStatisticsModel
from atriumsports.datacore.openapi.models.fixture_person_statistics_model_organization import (
    FixturePersonStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.fixture_person_statistics_periods_model import (
    FixturePersonStatisticsPeriodsModel,
)
from atriumsports.datacore.openapi.models.fixture_person_statistics_periods_model_organization import (
    FixturePersonStatisticsPeriodsModelOrganization,
)
from atriumsports.datacore.openapi.models.fixture_person_statistics_periods_post_body import (
    FixturePersonStatisticsPeriodsPostBody,
)
from atriumsports.datacore.openapi.models.fixture_person_statistics_periods_response import (
    FixturePersonStatisticsPeriodsResponse,
)
from atriumsports.datacore.openapi.models.fixture_person_statistics_post_body import FixturePersonStatisticsPostBody
from atriumsports.datacore.openapi.models.fixture_person_statistics_response import FixturePersonStatisticsResponse
from atriumsports.datacore.openapi.models.fixture_persons_model import FixturePersonsModel
from atriumsports.datacore.openapi.models.fixture_persons_model_organization import FixturePersonsModelOrganization
from atriumsports.datacore.openapi.models.fixture_persons_model_person import FixturePersonsModelPerson
from atriumsports.datacore.openapi.models.fixture_persons_post_body import FixturePersonsPostBody
from atriumsports.datacore.openapi.models.fixture_persons_response import FixturePersonsResponse
from atriumsports.datacore.openapi.models.fixture_post_body import FixturePostBody
from atriumsports.datacore.openapi.models.fixture_profiles_model import FixtureProfilesModel
from atriumsports.datacore.openapi.models.fixture_profiles_model_organization import FixtureProfilesModelOrganization
from atriumsports.datacore.openapi.models.fixture_profiles_post_body import FixtureProfilesPostBody
from atriumsports.datacore.openapi.models.fixture_profiles_put_body import FixtureProfilesPutBody
from atriumsports.datacore.openapi.models.fixture_profiles_response import FixtureProfilesResponse
from atriumsports.datacore.openapi.models.fixture_progression_post_body import FixtureProgressionPostBody
from atriumsports.datacore.openapi.models.fixture_progression_put_body import FixtureProgressionPutBody
from atriumsports.datacore.openapi.models.fixture_progressions_model import FixtureProgressionsModel
from atriumsports.datacore.openapi.models.fixture_progressions_model_fixture import FixtureProgressionsModelFixture
from atriumsports.datacore.openapi.models.fixture_progressions_model_organization import (
    FixtureProgressionsModelOrganization,
)
from atriumsports.datacore.openapi.models.fixture_progressions_model_season import FixtureProgressionsModelSeason
from atriumsports.datacore.openapi.models.fixture_progressions_response import FixtureProgressionsResponse
from atriumsports.datacore.openapi.models.fixture_put_body import FixturePutBody
from atriumsports.datacore.openapi.models.fixture_roster_model import FixtureRosterModel
from atriumsports.datacore.openapi.models.fixture_roster_model_organization import FixtureRosterModelOrganization
from atriumsports.datacore.openapi.models.fixture_roster_post_body import FixtureRosterPostBody
from atriumsports.datacore.openapi.models.fixture_roster_response import FixtureRosterResponse
from atriumsports.datacore.openapi.models.fixture_videosteam_post_body import FixtureVideosteamPostBody
from atriumsports.datacore.openapi.models.fixtures_by_competition_model import FixturesByCompetitionModel
from atriumsports.datacore.openapi.models.fixtures_by_competition_response import FixturesByCompetitionResponse
from atriumsports.datacore.openapi.models.fixtures_by_entity_model import FixturesByEntityModel
from atriumsports.datacore.openapi.models.fixtures_by_entity_response import FixturesByEntityResponse
from atriumsports.datacore.openapi.models.fixtures_model import FixturesModel
from atriumsports.datacore.openapi.models.fixtures_model_fixture_profile import FixturesModelFixtureProfile
from atriumsports.datacore.openapi.models.fixtures_model_organization import FixturesModelOrganization
from atriumsports.datacore.openapi.models.fixtures_model_round import FixturesModelRound
from atriumsports.datacore.openapi.models.fixtures_model_series import FixturesModelSeries
from atriumsports.datacore.openapi.models.fixtures_model_venue import FixturesModelVenue
from atriumsports.datacore.openapi.models.fixtures_response import FixturesResponse
from atriumsports.datacore.openapi.models.game_log_entity_model import GameLogEntityModel
from atriumsports.datacore.openapi.models.game_log_entity_model_organization import GameLogEntityModelOrganization
from atriumsports.datacore.openapi.models.game_log_entity_response import GameLogEntityResponse
from atriumsports.datacore.openapi.models.game_log_person_model import GameLogPersonModel
from atriumsports.datacore.openapi.models.game_log_person_model_organization import GameLogPersonModelOrganization
from atriumsports.datacore.openapi.models.game_log_person_response import GameLogPersonResponse
from atriumsports.datacore.openapi.models.head_to_head_identification import HeadToHeadIdentification
from atriumsports.datacore.openapi.models.head_to_head_identification_for_subsequent_checks import (
    HeadToHeadIdentificationForSubsequentChecks,
)
from atriumsports.datacore.openapi.models.head_to_head_resolution import HeadToHeadResolution
from atriumsports.datacore.openapi.models.head_to_head_resolution_for_extra_depth_h2h_s import (
    HeadToHeadResolutionForExtraDepthH2hS,
)
from atriumsports.datacore.openapi.models.images_model import ImagesModel
from atriumsports.datacore.openapi.models.images_model_organization import ImagesModelOrganization
from atriumsports.datacore.openapi.models.images_post_body import ImagesPostBody
from atriumsports.datacore.openapi.models.images_put_body import ImagesPutBody
from atriumsports.datacore.openapi.models.images_response import ImagesResponse
from atriumsports.datacore.openapi.models.included_data import IncludedData
from atriumsports.datacore.openapi.models.leader_criteria_model import LeaderCriteriaModel
from atriumsports.datacore.openapi.models.leader_criteria_model_organization import LeaderCriteriaModelOrganization
from atriumsports.datacore.openapi.models.leader_criteria_post_body import LeaderCriteriaPostBody
from atriumsports.datacore.openapi.models.leader_criteria_put_body import LeaderCriteriaPutBody
from atriumsports.datacore.openapi.models.leader_criteria_response import LeaderCriteriaResponse
from atriumsports.datacore.openapi.models.leader_qualifier_post_body import LeaderQualifierPostBody
from atriumsports.datacore.openapi.models.leader_qualifier_put_body import LeaderQualifierPutBody
from atriumsports.datacore.openapi.models.leader_qualifiers_model import LeaderQualifiersModel
from atriumsports.datacore.openapi.models.leader_qualifiers_model_leaders_criteria import (
    LeaderQualifiersModelLeadersCriteria,
)
from atriumsports.datacore.openapi.models.leader_qualifiers_model_organization import LeaderQualifiersModelOrganization
from atriumsports.datacore.openapi.models.leader_qualifiers_response import LeaderQualifiersResponse
from atriumsports.datacore.openapi.models.leader_summary_model import LeaderSummaryModel
from atriumsports.datacore.openapi.models.leader_summary_response import LeaderSummaryResponse
from atriumsports.datacore.openapi.models.league_external_ids_model import LeagueExternalIdsModel
from atriumsports.datacore.openapi.models.league_external_ids_model_league import LeagueExternalIdsModelLeague
from atriumsports.datacore.openapi.models.league_external_ids_model_organization import (
    LeagueExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.league_external_ids_post_body import LeagueExternalIdsPostBody
from atriumsports.datacore.openapi.models.league_external_ids_put_body import LeagueExternalIdsPutBody
from atriumsports.datacore.openapi.models.league_external_ids_response import LeagueExternalIdsResponse
from atriumsports.datacore.openapi.models.league_post_body import LeaguePostBody
from atriumsports.datacore.openapi.models.league_put_body import LeaguePutBody
from atriumsports.datacore.openapi.models.leagues_model import LeaguesModel
from atriumsports.datacore.openapi.models.leagues_model_organization import LeaguesModelOrganization
from atriumsports.datacore.openapi.models.leagues_response import LeaguesResponse
from atriumsports.datacore.openapi.models.organization_post_body import OrganizationPostBody
from atriumsports.datacore.openapi.models.organization_put_body import OrganizationPutBody
from atriumsports.datacore.openapi.models.organizations_model import OrganizationsModel
from atriumsports.datacore.openapi.models.organizations_response import OrganizationsResponse
from atriumsports.datacore.openapi.models.person_additional_details import PersonAdditionalDetails
from atriumsports.datacore.openapi.models.person_external_ids_model import PersonExternalIdsModel
from atriumsports.datacore.openapi.models.person_external_ids_model_organization import (
    PersonExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.person_external_ids_post_body import PersonExternalIdsPostBody
from atriumsports.datacore.openapi.models.person_external_ids_put_body import PersonExternalIdsPutBody
from atriumsports.datacore.openapi.models.person_external_ids_response import PersonExternalIdsResponse
from atriumsports.datacore.openapi.models.person_historical_name import PersonHistoricalName
from atriumsports.datacore.openapi.models.person_list_default_response import PersonListDefaultResponse
from atriumsports.datacore.openapi.models.person_post_body import PersonPostBody
from atriumsports.datacore.openapi.models.person_post_body_additional_names_value import (
    PersonPostBodyAdditionalNamesValue,
)
from atriumsports.datacore.openapi.models.person_put_body import PersonPutBody
from atriumsports.datacore.openapi.models.persons_model import PersonsModel
from atriumsports.datacore.openapi.models.persons_model_organization import PersonsModelOrganization
from atriumsports.datacore.openapi.models.persons_response import PersonsResponse
from atriumsports.datacore.openapi.models.pool_post_body import PoolPostBody
from atriumsports.datacore.openapi.models.pool_put_body import PoolPutBody
from atriumsports.datacore.openapi.models.ranking_rows_model import RankingRowsModel
from atriumsports.datacore.openapi.models.ranking_rows_post_body import RankingRowsPostBody
from atriumsports.datacore.openapi.models.ranking_rows_put_body import RankingRowsPutBody
from atriumsports.datacore.openapi.models.ranking_rows_response import RankingRowsResponse
from atriumsports.datacore.openapi.models.response_links import ResponseLinks
from atriumsports.datacore.openapi.models.response_meta_data import ResponseMetaData
from atriumsports.datacore.openapi.models.role_post_body import RolePostBody
from atriumsports.datacore.openapi.models.role_put_body import RolePutBody
from atriumsports.datacore.openapi.models.roles_model import RolesModel
from atriumsports.datacore.openapi.models.roles_model_organization import RolesModelOrganization
from atriumsports.datacore.openapi.models.roles_response import RolesResponse
from atriumsports.datacore.openapi.models.round_post_body import RoundPostBody
from atriumsports.datacore.openapi.models.round_put_body import RoundPutBody
from atriumsports.datacore.openapi.models.season_entities_list_model import SeasonEntitiesListModel
from atriumsports.datacore.openapi.models.season_entities_list_model_organization import (
    SeasonEntitiesListModelOrganization,
)
from atriumsports.datacore.openapi.models.season_entities_list_response import SeasonEntitiesListResponse
from atriumsports.datacore.openapi.models.season_entities_model import SeasonEntitiesModel
from atriumsports.datacore.openapi.models.season_entities_post_body import SeasonEntitiesPostBody
from atriumsports.datacore.openapi.models.season_entities_response import SeasonEntitiesResponse
from atriumsports.datacore.openapi.models.season_entity_base_statistics_model import SeasonEntityBaseStatisticsModel
from atriumsports.datacore.openapi.models.season_entity_base_statistics_model_organization import (
    SeasonEntityBaseStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.season_entity_base_statistics_post_body import (
    SeasonEntityBaseStatisticsPostBody,
)
from atriumsports.datacore.openapi.models.season_entity_base_statistics_response import (
    SeasonEntityBaseStatisticsResponse,
)
from atriumsports.datacore.openapi.models.season_entity_placings_model import SeasonEntityPlacingsModel
from atriumsports.datacore.openapi.models.season_entity_placings_response import SeasonEntityPlacingsResponse
from atriumsports.datacore.openapi.models.season_entity_statistics_model import SeasonEntityStatisticsModel
from atriumsports.datacore.openapi.models.season_entity_statistics_model_organization import (
    SeasonEntityStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.season_entity_statistics_response import SeasonEntityStatisticsResponse
from atriumsports.datacore.openapi.models.season_external_ids_model import SeasonExternalIdsModel
from atriumsports.datacore.openapi.models.season_external_ids_model_organization import (
    SeasonExternalIdsModelOrganization,
)
from atriumsports.datacore.openapi.models.season_external_ids_post_body import SeasonExternalIdsPostBody
from atriumsports.datacore.openapi.models.season_external_ids_put_body import SeasonExternalIdsPutBody
from atriumsports.datacore.openapi.models.season_external_ids_response import SeasonExternalIdsResponse
from atriumsports.datacore.openapi.models.season_fixture_stages_pools_list_model import (
    SeasonFixtureStagesPoolsListModel,
)
from atriumsports.datacore.openapi.models.season_fixture_stages_pools_list_model_organization import (
    SeasonFixtureStagesPoolsListModelOrganization,
)
from atriumsports.datacore.openapi.models.season_fixture_stages_pools_list_model_pool import (
    SeasonFixtureStagesPoolsListModelPool,
)
from atriumsports.datacore.openapi.models.season_fixture_stages_pools_list_model_stage import (
    SeasonFixtureStagesPoolsListModelStage,
)
from atriumsports.datacore.openapi.models.season_fixture_stages_pools_list_response import (
    SeasonFixtureStagesPoolsListResponse,
)
from atriumsports.datacore.openapi.models.season_person_base_statistics_model import SeasonPersonBaseStatisticsModel
from atriumsports.datacore.openapi.models.season_person_base_statistics_model_organization import (
    SeasonPersonBaseStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.season_person_base_statistics_post_body import (
    SeasonPersonBaseStatisticsPostBody,
)
from atriumsports.datacore.openapi.models.season_person_base_statistics_response import (
    SeasonPersonBaseStatisticsResponse,
)
from atriumsports.datacore.openapi.models.season_person_placings_model import SeasonPersonPlacingsModel
from atriumsports.datacore.openapi.models.season_person_placings_response import SeasonPersonPlacingsResponse
from atriumsports.datacore.openapi.models.season_person_statistics_model import SeasonPersonStatisticsModel
from atriumsports.datacore.openapi.models.season_person_statistics_model_organization import (
    SeasonPersonStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.season_person_statistics_periods_model import (
    SeasonPersonStatisticsPeriodsModel,
)
from atriumsports.datacore.openapi.models.season_person_statistics_periods_response import (
    SeasonPersonStatisticsPeriodsResponse,
)
from atriumsports.datacore.openapi.models.season_person_statistics_response import SeasonPersonStatisticsResponse
from atriumsports.datacore.openapi.models.season_person_total_statistics_model import SeasonPersonTotalStatisticsModel
from atriumsports.datacore.openapi.models.season_person_total_statistics_model_organization import (
    SeasonPersonTotalStatisticsModelOrganization,
)
from atriumsports.datacore.openapi.models.season_person_total_statistics_response import (
    SeasonPersonTotalStatisticsResponse,
)
from atriumsports.datacore.openapi.models.season_persons_list_model import SeasonPersonsListModel
from atriumsports.datacore.openapi.models.season_persons_list_model_organization import (
    SeasonPersonsListModelOrganization,
)
from atriumsports.datacore.openapi.models.season_persons_list_response import SeasonPersonsListResponse
from atriumsports.datacore.openapi.models.season_persons_model import SeasonPersonsModel
from atriumsports.datacore.openapi.models.season_persons_post_body import SeasonPersonsPostBody
from atriumsports.datacore.openapi.models.season_persons_response import SeasonPersonsResponse
from atriumsports.datacore.openapi.models.season_pools_model import SeasonPoolsModel
from atriumsports.datacore.openapi.models.season_pools_model_organization import SeasonPoolsModelOrganization
from atriumsports.datacore.openapi.models.season_pools_response import SeasonPoolsResponse
from atriumsports.datacore.openapi.models.season_post_body import SeasonPostBody
from atriumsports.datacore.openapi.models.season_put_body import SeasonPutBody
from atriumsports.datacore.openapi.models.season_roster_model import SeasonRosterModel
from atriumsports.datacore.openapi.models.season_roster_model_organization import SeasonRosterModelOrganization
from atriumsports.datacore.openapi.models.season_roster_post_body import SeasonRosterPostBody
from atriumsports.datacore.openapi.models.season_roster_response import SeasonRosterResponse
from atriumsports.datacore.openapi.models.season_rounds_model import SeasonRoundsModel
from atriumsports.datacore.openapi.models.season_rounds_model_organization import SeasonRoundsModelOrganization
from atriumsports.datacore.openapi.models.season_rounds_response import SeasonRoundsResponse
from atriumsports.datacore.openapi.models.season_series_competitor import SeasonSeriesCompetitor
from atriumsports.datacore.openapi.models.season_series_model import SeasonSeriesModel
from atriumsports.datacore.openapi.models.season_series_model_organization import SeasonSeriesModelOrganization
from atriumsports.datacore.openapi.models.season_series_response import SeasonSeriesResponse
from atriumsports.datacore.openapi.models.season_stage_post_body import SeasonStagePostBody
from atriumsports.datacore.openapi.models.season_stage_put_body import SeasonStagePutBody
from atriumsports.datacore.openapi.models.season_stages_model import SeasonStagesModel
from atriumsports.datacore.openapi.models.season_stages_model_organization import SeasonStagesModelOrganization
from atriumsports.datacore.openapi.models.season_stages_response import SeasonStagesResponse
from atriumsports.datacore.openapi.models.season_standings_stages_pools_list_model import (
    SeasonStandingsStagesPoolsListModel,
)
from atriumsports.datacore.openapi.models.season_standings_stages_pools_list_model_organization import (
    SeasonStandingsStagesPoolsListModelOrganization,
)
from atriumsports.datacore.openapi.models.season_standings_stages_pools_list_response import (
    SeasonStandingsStagesPoolsListResponse,
)
from atriumsports.datacore.openapi.models.season_venues_address import SeasonVenuesAddress
from atriumsports.datacore.openapi.models.season_venues_list_model import SeasonVenuesListModel
from atriumsports.datacore.openapi.models.season_venues_list_model_organization import SeasonVenuesListModelOrganization
from atriumsports.datacore.openapi.models.season_venues_list_model_site import SeasonVenuesListModelSite
from atriumsports.datacore.openapi.models.season_venues_list_response import SeasonVenuesListResponse
from atriumsports.datacore.openapi.models.seasonentity_placings_post_body import SEASONENTITYPlacingsPostBody
from atriumsports.datacore.openapi.models.seasonentity_placings_put_body import SEASONENTITYPlacingsPutBody
from atriumsports.datacore.openapi.models.seasonperson_placings_post_body import SEASONPERSONPlacingsPostBody
from atriumsports.datacore.openapi.models.seasonperson_placings_put_body import SEASONPERSONPlacingsPutBody
from atriumsports.datacore.openapi.models.seasonroster_configuration import SEASONROSTERConfiguration
from atriumsports.datacore.openapi.models.seasons_model import SeasonsModel
from atriumsports.datacore.openapi.models.seasons_model_competition import SeasonsModelCompetition
from atriumsports.datacore.openapi.models.seasons_model_fixture_profile import SeasonsModelFixtureProfile
from atriumsports.datacore.openapi.models.seasons_model_organization import SeasonsModelOrganization
from atriumsports.datacore.openapi.models.seasons_model_standing_configuration import SeasonsModelStandingConfiguration
from atriumsports.datacore.openapi.models.seasons_response import SeasonsResponse
from atriumsports.datacore.openapi.models.series_post_body import SeriesPostBody
from atriumsports.datacore.openapi.models.series_put_body import SeriesPutBody
from atriumsports.datacore.openapi.models.site_address import SiteAddress
from atriumsports.datacore.openapi.models.site_external_ids_model import SiteExternalIdsModel
from atriumsports.datacore.openapi.models.site_external_ids_model_organization import SiteExternalIdsModelOrganization
from atriumsports.datacore.openapi.models.site_external_ids_model_site import SiteExternalIdsModelSite
from atriumsports.datacore.openapi.models.site_external_ids_post_body import SiteExternalIdsPostBody
from atriumsports.datacore.openapi.models.site_external_ids_put_body import SiteExternalIdsPutBody
from atriumsports.datacore.openapi.models.site_external_ids_response import SiteExternalIdsResponse
from atriumsports.datacore.openapi.models.site_post_body import SitePostBody
from atriumsports.datacore.openapi.models.site_put_body import SitePutBody
from atriumsports.datacore.openapi.models.sites_model import SitesModel
from atriumsports.datacore.openapi.models.sites_model_organization import SitesModelOrganization
from atriumsports.datacore.openapi.models.sites_response import SitesResponse
from atriumsports.datacore.openapi.models.social_media import SocialMedia
from atriumsports.datacore.openapi.models.sorting import Sorting
from atriumsports.datacore.openapi.models.standing_adjustment_post_body import StandingAdjustmentPostBody
from atriumsports.datacore.openapi.models.standing_adjustment_put_body import StandingAdjustmentPutBody
from atriumsports.datacore.openapi.models.standing_adjustments_model import StandingAdjustmentsModel
from atriumsports.datacore.openapi.models.standing_adjustments_model_organization import (
    StandingAdjustmentsModelOrganization,
)
from atriumsports.datacore.openapi.models.standing_adjustments_response import StandingAdjustmentsResponse
from atriumsports.datacore.openapi.models.standing_building import StandingBuilding
from atriumsports.datacore.openapi.models.standing_configuration import StandingConfiguration
from atriumsports.datacore.openapi.models.standing_configurations_model import StandingConfigurationsModel
from atriumsports.datacore.openapi.models.standing_configurations_model_organization import (
    StandingConfigurationsModelOrganization,
)
from atriumsports.datacore.openapi.models.standing_configurations_post_body import StandingConfigurationsPostBody
from atriumsports.datacore.openapi.models.standing_configurations_put_body import StandingConfigurationsPutBody
from atriumsports.datacore.openapi.models.standing_configurations_response import StandingConfigurationsResponse
from atriumsports.datacore.openapi.models.standing_post_body import StandingPostBody
from atriumsports.datacore.openapi.models.standing_post_body_calculated_value import StandingPostBodyCalculatedValue
from atriumsports.datacore.openapi.models.standing_post_body_points_value import StandingPostBodyPointsValue
from atriumsports.datacore.openapi.models.standing_put_body import StandingPutBody
from atriumsports.datacore.openapi.models.standings_model import StandingsModel
from atriumsports.datacore.openapi.models.standings_model_organization import StandingsModelOrganization
from atriumsports.datacore.openapi.models.standings_response import StandingsResponse
from atriumsports.datacore.openapi.models.success_model import SuccessModel
from atriumsports.datacore.openapi.models.success_response import SuccessResponse
from atriumsports.datacore.openapi.models.transfer_component import TransferComponent
from atriumsports.datacore.openapi.models.transfer_post_body import TransferPostBody
from atriumsports.datacore.openapi.models.transfer_put_body import TransferPutBody
from atriumsports.datacore.openapi.models.transfers_model import TransfersModel
from atriumsports.datacore.openapi.models.transfers_model_organization import TransfersModelOrganization
from atriumsports.datacore.openapi.models.transfers_response import TransfersResponse
from atriumsports.datacore.openapi.models.venue_address import VenueAddress
from atriumsports.datacore.openapi.models.venue_external_ids_model import VenueExternalIdsModel
from atriumsports.datacore.openapi.models.venue_external_ids_model_organization import VenueExternalIdsModelOrganization
from atriumsports.datacore.openapi.models.venue_external_ids_post_body import VenueExternalIdsPostBody
from atriumsports.datacore.openapi.models.venue_external_ids_put_body import VenueExternalIdsPutBody
from atriumsports.datacore.openapi.models.venue_external_ids_response import VenueExternalIdsResponse
from atriumsports.datacore.openapi.models.venue_historical_name import VenueHistoricalName
from atriumsports.datacore.openapi.models.venue_post_body import VenuePostBody
from atriumsports.datacore.openapi.models.venue_put_body import VenuePutBody
from atriumsports.datacore.openapi.models.venues_model import VenuesModel
from atriumsports.datacore.openapi.models.venues_model_organization import VenuesModelOrganization
from atriumsports.datacore.openapi.models.venues_model_site import VenuesModelSite
from atriumsports.datacore.openapi.models.venues_response import VenuesResponse
from atriumsports.datacore.openapi.models.video_file_post_body import VideoFilePostBody
from atriumsports.datacore.openapi.models.video_files_download_model import VideoFilesDownloadModel
from atriumsports.datacore.openapi.models.video_files_download_response import VideoFilesDownloadResponse
from atriumsports.datacore.openapi.models.video_files_model import VideoFilesModel
from atriumsports.datacore.openapi.models.video_files_model_organization import VideoFilesModelOrganization
from atriumsports.datacore.openapi.models.video_files_response import VideoFilesResponse
from atriumsports.datacore.openapi.models.video_stream_inputs_model import VideoStreamInputsModel
from atriumsports.datacore.openapi.models.video_stream_inputs_model_organization import (
    VideoStreamInputsModelOrganization,
)
from atriumsports.datacore.openapi.models.video_stream_inputs_response import VideoStreamInputsResponse
from atriumsports.datacore.openapi.models.video_stream_local_model import VideoStreamLocalModel
from atriumsports.datacore.openapi.models.video_stream_local_model_organization import VideoStreamLocalModelOrganization
from atriumsports.datacore.openapi.models.video_stream_local_post_body import VideoStreamLocalPostBody
from atriumsports.datacore.openapi.models.video_stream_local_put_body import VideoStreamLocalPutBody
from atriumsports.datacore.openapi.models.video_stream_local_response import VideoStreamLocalResponse
from atriumsports.datacore.openapi.models.video_stream_outputs_model import VideoStreamOutputsModel
from atriumsports.datacore.openapi.models.video_stream_outputs_model_organization import (
    VideoStreamOutputsModelOrganization,
)
from atriumsports.datacore.openapi.models.video_stream_outputs_response import VideoStreamOutputsResponse
from atriumsports.datacore.openapi.models.video_subscription_post_body import VideoSubscriptionPostBody
from atriumsports.datacore.openapi.models.video_subscription_put_body import VideoSubscriptionPutBody
from atriumsports.datacore.openapi.models.video_subscriptions_model import VideoSubscriptionsModel
from atriumsports.datacore.openapi.models.video_subscriptions_model_organization import (
    VideoSubscriptionsModelOrganization,
)
from atriumsports.datacore.openapi.models.video_subscriptions_response import VideoSubscriptionsResponse
