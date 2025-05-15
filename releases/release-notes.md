## Release Notes for MATLAB Web App Server on Amazon Web Services

### R2025a
- You can now deploy MATLAB Web App Server R2025a using the Amazon Web Services reference architecture.
- You can now manage MATLAB Web App Server Linux instances using the MATLAB Web App Server Admin Portal, which is a web-based interface to edit server settings, configure access control for web applications, and view server logs. For more details, see [Connect and Log In to the Admin Portal](R2025a/README.md#step-6-connect-and-log-in-to-the-admin-portal-linux-server-only).
- On Linux servers, user authentication to the admin portal and MATLAB Web App Server home page is administered by default through [Keycloak](https://www.keycloak.org/docs/latest/server_admin/index.html). Keycloak is a cloud native solution that provides authentication, authorization, and user management for applications and services. You can configure authentication using your identity provider with Keycloak or directly using LDAP or OIDC. For more details, see [Configure User Authentication](R2025a/README.md#step-8-configure-user-authentication).
