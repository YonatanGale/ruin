
--auditoria Insert categorymaterials
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CATEGORYMATERIALS
AFTER INSERT ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria (tabla, accion, datos_viejos, datos_nuevos, usuario, fecha) 
    VALUES ('erp_categorymaterials', 'I', NULL, (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.unity, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), NEW.user_create, date('now'));
END;

--auditoria update categorymaterials
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CATEGORYMATERIALS
AFTER UPDATE ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_categorymaterials', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.unity, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.unity, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--auditoria DELETE categorymaterials
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_CATEGORYMATERIALS
AFTER DELETE ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria 
    (tabla, 
    accion, 
    datos_viejos, 
    datos_nuevos, 
    usuario, 
    fecha
    )
     
    VALUES 
    ('erp_categorymaterials', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.unity, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;