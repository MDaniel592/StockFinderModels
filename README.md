# stockfinder_models

Repository base of models for sqlalchemy
This repo is cloned in multiple other repos / projects

# Updated_at needs a trigger

Reference: https://stackoverflow.com/questions/34818544/postgresql-how-to-add-multiple-table-for-one-trigger
## Tables with updated_at
- alerts
- messages
- products
- products_availabilities
- roles
- specs
- telegram_channels
- users

### Trigger Function 
```
CREATE OR REPLACE FUNCTION updated_timestamp_func()
RETURNS TRIGGER
LANGUAGE plpgsql AS
'
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
';
```
### Trigger on each table with updated_at

```
DO $$
DECLARE
    t text;
BEGIN
    FOR t IN
        SELECT table_name FROM information_schema.columns WHERE column_name = 'updated_at'
    LOOP
        EXECUTE format('CREATE TRIGGER trigger_update_timestamp
                    BEFORE UPDATE ON %I
                    FOR EACH ROW EXECUTE PROCEDURE updated_timestamp_func()', t,t);
    END loop;
END;
$$ language 'plpgsql';
```