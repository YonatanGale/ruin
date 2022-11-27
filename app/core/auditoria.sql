
--AUDITORIA INSERT CATEGORYMATERIALS
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CATEGORYMATERIALS
AFTER INSERT ON erp_categorymaterials
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_categorymaterials', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.unity, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), 
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CATEGORYMATERIALS
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

--AUDITORIA DELETE CATEGORYMATERIALS
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

--AUDITORIA INSERT BUY

CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_BUY
AFTER INSERT ON erp_buy
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_buy', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.iva, '')|| ',' || IFNULL(NEW.total, '')|| ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.prov_id, '') || ',' || IFNULL(NEW.methodpay_id, '')|| ',' || IFNULL(NEW.typfund_id, '')|| ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), 
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE BUY
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_BUY
AFTER UPDATE ON erp_buy
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
    ('erp_buy', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.iva, '')|| ',' || IFNULL(OLD.total, '')|| ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.prov_id, '') || ',' || IFNULL(OLD.methodpay_id, '')|| ',' || IFNULL(OLD.typfund_id, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || OLD.user_create|| ',' || IFNULL(OLD.user_update, '')  ),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.iva, '')|| ',' || IFNULL(NEW.total, '')|| ',' || IFNULL(NEW.subtotal, '')|| ',' || IFNULL(NEW.prov_id, '') || ',' || IFNULL(NEW.methodpay_id, '')|| ',' || IFNULL(NEW.typfund_id, '')|| ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ), 
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE BUY
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_BUY
AFTER DELETE ON erp_buy
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
    ('erp_buy', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.iva, '')|| ',' || IFNULL(OLD.total, '')|| ',' || IFNULL(OLD.subtotal, '')|| ',' || IFNULL(OLD.prov_id, '') || ',' || IFNULL(OLD.methodpay_id, '')|| ',' || IFNULL(OLD.typfund_id, '')|| ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || OLD.user_create|| ',' || IFNULL(OLD.user_update, '')  ),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT CATEGORY
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CATEGORY
AFTER INSERT ON erp_category
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_category', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CATEGORY

CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CATEGORY
AFTER UPDATE ON erp_category
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
    ('erp_category', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.name, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE CATEGORY

CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_CATEGORY
AFTER DELETE ON erp_category
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
    ('erp_category', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.name, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT CIERRECAJA
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CIERRECAJA
AFTER INSERT ON erp_cierrecaja
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_cierrecaja', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.typeF_id, '') || ',' || IFNULL(NEW.tot, '') || ',' || IFNULL(NEW.estado, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CIERRECAJA

CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CIERRECAJA
AFTER UPDATE ON erp_cierrecaja
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
    ('erp_cierrecaja', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.typeF_id, '') || ',' || IFNULL(OLD.tot, '') || ',' || IFNULL(OLD.estado, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.typeF_id, '') || ',' || IFNULL(NEW.tot, '') || ',' || IFNULL(NEW.estado, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT CLIENTE
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_CLIENT
AFTER INSERT ON erp_client
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_client', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.names, '') || ',' || IFNULL(NEW.surnames, '') || ',' || IFNULL(NEW.ci, '') || ',' || IFNULL(NEW.Birthday, '') || ',' || IFNULL(NEW.addres, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE CLIENTE
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_CLIENTE
AFTER UPDATE ON erp_client
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
    ('erp_client', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.names, '') || ',' || IFNULL(OLD.surnames, '') || ',' || IFNULL(OLD.Birthday, '') || ',' || IFNULL(OLD.addres, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.names, '') || ',' || IFNULL(NEW.surnames, '') || ',' || IFNULL(NEW.Birthday, '') || ',' || IFNULL(NEW.addres, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE CLIENTE
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_CLIENT
AFTER DELETE ON erp_client
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
    ('erp_client', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.names, '') || ',' || IFNULL(OLD.surnames, '') || ',' || IFNULL(OLD.ci, '') || ',' || IFNULL(OLD.Birthday, '') || ',' || IFNULL(OLD.addres, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT DETBUY
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_DET_BUY
AFTER INSERT ON erp_detbuy
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_detbuy', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.price, '') || ',' || IFNULL(NEW.cant, '') || ',' || IFNULL(NEW.subtotal, '') || ',' || IFNULL(NEW.buy_id, '') || ',' || IFNULL(NEW.prod_id, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;


--AUDITORIA INSERT PRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDINSERT_ERP_PRODUCTION
AFTER INSERT ON erp_production
BEGIN
    INSERT INTO erp_auditoria (
        tabla, 
        accion, 
        datos_viejos, 
        datos_nuevos, 
        usuario, 
        fecha) 
    VALUES (
        'erp_production', 
        'I', 
        NULL, 
        (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.produc_id, '') || ',' || IFNULL(NEW.total, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || NEW.user_create|| ',' || IFNULL(NEW.user_update, '')  ),  
        NEW.user_create, 
        date('now'));
END;

--AUDITORIA UPDATE PRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDUPDATE_ERP_PRODUCTION
AFTER UPDATE ON erp_production
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
    ('erp_production', 
    'U', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.produc_id, '') || ',' || IFNULL(OLD.total, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    (IFNULL(NEW.id, '') || ',' || IFNULL(NEW.date_joined, '') || ',' || IFNULL(NEW.produc_id, '') || ',' || IFNULL(NEW.total, '') || ',' || IFNULL(NEW.date_create, '') || ',' || IFNULL(NEW.date_update, '') || ',' || IFNULL(NEW.user_create, '')|| ',' || IFNULL(NEW.user_update, '')),
    NEW.user_update, 
    date('now')
    );
END;

--AUDITORIA DELETE PRODUCTIONS
CREATE TRIGGER IF NOT EXISTS AUDDELETE_ERP_PRODUCTION
AFTER DELETE ON erp_production
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
    ('erp_production', 
    'D', 
    (IFNULL(OLD.id, '') || ',' || IFNULL(OLD.date_joined, '') || ',' || IFNULL(OLD.produc_id, '') || ',' || IFNULL(OLD.total, '') || ',' || IFNULL(OLD.date_create, '') || ',' || IFNULL(OLD.date_update, '') || ',' || IFNULL(OLD.user_create, '')|| ',' || IFNULL(OLD.user_update, '')),
    NULL,
    OLD.user_update, 
    date('now')
    );
END;

--AUDITORIA INSERT DETPRODUCTIONS
