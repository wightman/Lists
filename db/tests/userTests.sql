/* userTests.sql
 *
 * Assuming an existing Users table
 */
 /* add a user as admin (succeed)*/
 CALL addUser('You', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
 /* - add a user as non-admin (FAIL) To be done at the application level
 * - add an existing user (FAIL)
 */
 CALL addUser('You', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
 /* update an admin status (succeed)*/
 CALL putUserAdmin(1, false);

 /* - update an admin status as non-admin (FAIL)  To be done at the application level
 /* update password (succeed) */
CALL putUserPassword(2,'$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetdI7P3q.5aWOHOO!');
 /* - update password as admin (succeed)  To be done at the application level
 * - update password as non-admin, non-user (FAIL)  To be done at the application level
 */

 /* - update a non-existing user (FAIL)*/
CALL putUser(666, 'wightman','me@you.com',true);

 *
 * - remove non-existing record as admin (FAIL)
 * - remove existing user as the user (succeed)
 * - remove existing user as admin (succeed)
 * - remove existing user as anyone (FAIL)
 */
