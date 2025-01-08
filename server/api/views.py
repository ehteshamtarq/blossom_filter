from django.http import JsonResponse
from .models import BlossomFilter, UniqueNumberCount, BlossomFilterRecord
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def unique_number(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        unique_num = data.get('unique_number')
        unique_num_count_id = data.get('unique_number_count_id')

        if unique_num:
            if unique_num_count_id:
                try:
                    unique_number_count = UniqueNumberCount.objects.get(id=unique_num_count_id)
                except UniqueNumberCount.DoesNotExist:
                    return JsonResponse({'error': 'Invalid unique_number_count_id'}, status=400)
            else:
                unique_number_count = UniqueNumberCount.objects.create()

            filter_record, created = BlossomFilterRecord.objects.get_or_create(
                unique_number_count=unique_number_count,
                defaults={"blossom_filter": BlossomFilter(size=100).serialize()}
            )

            filter_instance = filter_record.load_blossom_filter()

            if filter_instance.check(unique_num):
                return JsonResponse({
                    'unique_number_count': unique_number_count.count,
                    'unique_number_count_id': unique_number_count.id
                })

            filter_instance.add(unique_num)

            filter_record.save_blossom_filter(filter_instance)

            unique_number_count.increment_count()

            return JsonResponse({
                'unique_number_count': unique_number_count.count,
                'unique_number_count_id': unique_number_count.id
            })

        return JsonResponse({'error': 'Invalid request'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def check_number_in_filter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        unique_num = data.get('unique_number')
        unique_num_count_id = data.get('unique_number_count_id')

        if unique_num_count_id:
            try:
                unique_number_count = UniqueNumberCount.objects.get(id=unique_num_count_id)
            except UniqueNumberCount.DoesNotExist:
                return JsonResponse({'error': 'Invalid unique_number_count_id'}, status=400)

            try:
                filter_record = BlossomFilterRecord.objects.get(unique_number_count=unique_number_count)
                filter_instance = filter_record.load_blossom_filter()

                if filter_instance.check(unique_num):
                    return JsonResponse({'exists': True}, status=200)
                else:
                    return JsonResponse({'exists': False}, status=200)

            except BlossomFilterRecord.DoesNotExist:
                return JsonResponse({'error': 'Number not found in any filter'}, status=404)

        return JsonResponse({'error': 'unique_number_count_id is required'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)
