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

 /* Get user info for userId = 1 */
 CALL getUser(1);
/* for non-existing userId */
CALL getUser(666);

 /* - update an admin status as non-admin (FAIL)  To be done at the application level
 /* update password (succeed) */
CALL putUserPassword(1,'$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetdI7P3q.5aWOHOO!');
 /* - update password as admin (succeed)  To be done at the application level
 * - update password as non-admin, non-user (FAIL)  To be done at the application level
 */

CALL putUser(1, 'wightman','you@unb.ca');
 /* - update a non-existing user (FAIL)*/
CALL putUser(666, 'wightman','me@you.com');

CALL addUser('Me', 'me@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
/* Should not be able to add/put existing email (FAIL) */
CALL addUser('Me', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL putUser(4, 'wightman','you@unb.ca');

/* get all user names */
CALL getUserNames();

/* delete existing user */
CALL delUser(4);
/* delete non-existing user (FAIL) */
CALL delUser(4);

/* list all user info, except password */
CALL getUsersAll();

/* verify password for a user */
CALL verifyUser('you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetdI7P3q.5aWOHOO!');
