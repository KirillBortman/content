from CommonServerPython import *

name_to_url = {
    'C2 IP Feed': 'http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist.txt',
    'High-Confidence C2 IP Feed': 'http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist-high.txt',
    'C2 Domain Feed': 'http://osint.bambenekconsulting.com/feeds/c2-dommasterlist.txt',
    'High-Confidence C2 Domain Feed': 'http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt',
    'DGA Domain Feed': 'https://faf.bambenekconsulting.com/feeds/dga-feed.gz',
    'High-Confidence DGA Domain Feed': 'https://faf.bambenekconsulting.com/feeds/dga-feed-high.gz',
    'C2 All Indicator Feed': 'https://faf.bambenekconsulting.com/feeds/dga/c2-masterlist.txt',
    'High-Confidence C2 All Indicator Feed': 'https://faf.bambenekconsulting.com/feeds/dga/c2-masterlist-high.txt',
    'Sinkhole Feed': 'https://faf.bambenekconsulting.com/feeds/sinkhole/latest.csv'
}


def main():
    feed_url_to_config = {
        'http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist.txt': {
            'fieldnames': ['value', 'description',
                           'date_created',
                           'info'],
            'indicator_type': FeedIndicatorType.IP,
            'mapping': {
                'description': 'malwarefamily'
            }
        },

        'http://osint.bambenekconsulting.com/feeds/c2-dommasterlist.txt': {
            'fieldnames': ['value', 'description',
                           'date_created',
                           'info'],
            'indicator_type': FeedIndicatorType.Domain,
            'mapping': {
                'description': 'malwarefamily'
            }
        },
        'http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist-high.txt': {
            'fieldnames': ['value', 'description',
                           'date_created',
                           'info'],
            'indicator_type': FeedIndicatorType.IP,
            'mapping': {
                'description': 'malwarefamily'
            }
        },
        'http://osint.bambenekconsulting.com/feeds/c2-dommasterlist-high.txt': {
            'fieldnames': ['value', 'description',
                           'date_created',
                           'info'],
            'indicator_type': FeedIndicatorType.Domain,
            'mapping': {
                'description': 'malwarefamily'
            }
        },
        'https://faf.bambenekconsulting.com/feeds/dga-feed.gz': {
            'fieldnames': ['value', 'description',
                           'date_created',
                           'info'],
            'indicator_type': FeedIndicatorType.Domain,
            'mapping': {
                'description': 'malwarefamily'
            },
            'is_zipped_file': True
        },
        'https://faf.bambenekconsulting.com/feeds/dga-feed-high.gz': {
            'fieldnames': ['value', 'description',
                           'date_created',
                           'info'],
            'indicator_type': FeedIndicatorType.Domain,
            'mapping': {
                'description': 'malwarefamily'
            },
            'is_zipped_file': True
        },
        'https://faf.bambenekconsulting.com/feeds/dga/c2-masterlist.txt': {
            'fieldnames': ['value',
                           'ip',
                           'nsname',
                           'nsip',
                           'description',
                           'info'],
            'indicator_type': FeedIndicatorType.Domain,
            'mapping': {
                'description': 'malwarefamily'
            }
        },
        'https://faf.bambenekconsulting.com/feeds/dga/c2-masterlist-high.txt': {
            'fieldnames': ['value',
                           'ip',
                           'nsname',
                           'nsip',
                           'description',
                           'info'],
            'indicator_type': FeedIndicatorType.Domain,
            'mapping': {
                'description': 'malwarefamily'
            }
        },
        'https://faf.bambenekconsulting.com/feeds/sinkhole/latest.csv': {
            'fieldnames': ['value',
                           'owner'],
            'indicator_type': FeedIndicatorType.IP,
        }
    }
    params = {k: v for k, v in demisto.params().items() if v is not None}
    params['url'] = [name_to_url.get(url) for url in argToList(params.get('url'))]
    params['feed_url_to_config'] = feed_url_to_config
    params['ignore_regex'] = r'^#'
    params['delimiter'] = ','

    # Main execution of the CSV API Module.
    # This function allows to add to or override this execution.
    feed_main('Bambenek Consulting Feed', params, 'bambenek')


from CSVFeedApiModule import *  # noqa: E402

if __name__ == '__builtin__' or __name__ == 'builtins':
    main()
