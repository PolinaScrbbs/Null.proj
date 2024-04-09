from django.contrib import admin
from .models import UserRole, User, OrganizationMemberRole, OrganizationMember, Organization

@admin.register(UserRole)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ('username', 'role')

@admin.register(OrganizationMemberRole)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(OrganizationMember)
class UserAdmin(admin.ModelAdmin):
    list_display = ('organization', 'user', 'role')
    search_fields = ('organization', 'user', 'role')

@admin.register(Organization)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','owner', 'members_count')
    search_fields = ('name','owner', 'members_count')

    def owner(self, obj):
        return OrganizationMember.objects.filter(organization=obj, user__role=1).first().user
    
    def members_count(self, obj):
        return OrganizationMember.objects.filter(organization=obj).count()
         
    def save_model(self, request, obj, form, change):
            if not change:
                obj.save()
                owner_role = OrganizationMemberRole.objects.get(id=1)  # Предполагается, что id роли создателя равно 1
                OrganizationMember.objects.create(user=request.user, organization=obj, role=owner_role)
            else:
                obj.save()