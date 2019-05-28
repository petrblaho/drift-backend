from prometheus_client import Counter, Histogram

api_exceptions = Counter("drift_inventory_service_exceptions",
                         "count of exceptions raised on public API")

systems_compared = Histogram("drift_systems_compared",
                             "count of systems compared in each request",
                             buckets=[2, 4, 8, 16, 32, 64, 128, 256])

systems_compared_no_sysprofile = Histogram("drift_systems_compared_no_sysprofile",
                                           "count of systems without system profile"
                                           "compared in each request",
                                           buckets=[2, 4, 8, 16, 32, 64, 128, 256])

comparison_report_requests = Histogram("drift_comparison_report_requests",
                                       "comparison report request stats")

inventory_service_requests = Histogram("drift_inventory_service_requests",
                                       "inventory service call stats")
