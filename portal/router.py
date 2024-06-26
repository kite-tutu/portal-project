class PortalRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on portal models to 'coopdb'"
        if model._meta.app_label == 'portal':
            return 'coopdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on portal models to 'coopdb'"
        if model._meta.app_label == 'portal':
            return 'coopdb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in portal app"
        if obj1._meta.app_label == 'portal' and obj2._meta.app_label == 'portal':
            return True
        # Allow if neither is portal app
        elif 'portal' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'coopdb' or model._meta.app_label == "portal":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True