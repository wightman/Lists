/* userTests.sql
 *
 * Assuming an existing Users table
 * - add a user as admin (succeed)
 * - add a user as non-admin (FAIL)
 * - add an existing user as admin (FAIL)
 *
 * - update an admin status as admin (succeed)
 * - update an admin status as non-admin (FAIL)
 *
 * - update password as user (succeed)
 * - update password as admin (succeed)
 * - update password as non-admin, non-user (FAIL)
 *
 * - update a non-existing user as anyone (FAIL)
 *
 * - remove non-existing record as admin (FAIL)
 * - remove existing user as the user (succeed)
 * - remove existing user as admin (succeed)
 * - remove existing user as anyone (FAIL)
 */
