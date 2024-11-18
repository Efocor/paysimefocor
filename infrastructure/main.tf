provider "google" {
  project = "your-gcp-project-id"  # Cambia a tu proyecto de GCP
  region  = "us-central1"
}

resource "google_container_cluster" "default" {
  name               = "payment-cluster"
  location           = "us-central1-a"
  initial_node_count = 3
}

resource "google_sql_database_instance" "default" {
  name = "payment-db"
  region = "us-central1"

  settings {
    tier = "db-f1-micro"
    backup_configuration {
      enabled = true
    }
  }
}

resource "google_sql_database" "default" {
  name     = "paymentdb"
  instance_name = google_sql_database_instance.default.name
}
