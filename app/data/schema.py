# app/data/schema.py

from . import incidents, datasets, tickets


def initialise_all_tables():
    print("Loading cyber incidents...")
    incidents.load_incidents_from_csv()
    print("Done.")

    print("Loading datasets metadata...")
    datasets.load_datasets_from_csv()
    print("Done.")

    print("Loading IT tickets...")
    tickets.load_tickets_from_csv()
    print("Done.")

    # Print summary
    print("\nSummary:")
    print("Incidents:", incidents.get_incident_count())
    print("Datasets:", datasets.get_dataset_count())
    print("Tickets:", tickets.get_ticket_count())