-- Enable the dblink extension if it's not already enabled
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_extension WHERE extname = 'dblink') THEN
       CREATE EXTENSION dblink;
   END IF;
END
$$;

-- Create the inventory contrib only if it does not already exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'app_scrape') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE app_scrape');
   END IF;
END
$$;

-- Create the inventory_test contrib only if it does not already exist
DO
$$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'app_scrape_test') THEN
       PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE app_scrape_test');
   END IF;
END
$$;
