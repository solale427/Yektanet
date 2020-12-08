from django.db.models import Subquery, OuterRef, Avg, F, DurationField

from advertiser_management.models import Click, AdView


def get_clicks_to_views_ratio_per_hour():
    clicks_per_hour = Click.get_clicks_sum_per_hour()
    views_per_hour = AdView.get_views_sum_per_hour()

    click_statistics = {
        (click_data['ad'], click_data['hour']): click_data for click_data in clicks_per_hour
    }

    result = []
    for item in list(views_per_hour):
        views = item['views']
        clicks = click_statistics.get((item['ad'], item['hour']), {}).get('clicks', 0)
        result.append({
            'ratio': clicks / views,
            'ad_id': item['ad'],
            'hour': item['hour'],
        })

    result = sorted(result, key=lambda ratio_data: ratio_data['hour'])
    return result


def click_to_view_avg_duration():
    duration_average = Click.objects.all().annotate(
        duration=Subquery(
            AdView.objects.filter(
                ad_id=OuterRef('ad_id'),
                user_ip=OuterRef('user_ip'),
                time__lte=OuterRef('time'),
            ).annotate(
                duration=OuterRef('time') - F('time')
            ).order_by('duration').values('duration')[:1],
        )
    ).aggregate(view_to_click_average=Avg('duration', output_field=DurationField()))['view_to_click_average']
    return duration_average
