/* usersTests.sql
 *
 * R Wightman, Dec 2017
 *
 * Assuming an existing Users table.
 * Restricted Admin operations are dealt with at the application level.
 */

/* Collection operations ---------------------------------------------------- */
/*
 * Get a list of all users (no passwords of course!)
*/
CALL getUsersAll();

/*
 * Get a list of users by admin status (no passwords of course!)
 */
CALL getUsersByAdmin(True);
CALL getUsersByAdmin(False);

/*
 * Get a list of all users with a string as part of the display name
 * (no passwords of course!)
 */
CALL getUsersByName('Rick');

/*
 * Get a list of all users with a string as part of the email address
 * (no passwords of course!)
 */
CALL getUsersByEmail('@example.ca');

/* Individual operations --------------------------------------------------- */

/*
 * Add a user (succeed)
 */
CALL addUser('You', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);

/*
 * Add an existing user (FAIL)
 */
CALL addUser('You', 'you@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);

/*
 * Get a user, but not the password (succeed).
 */
 CALL getUser(<id-from-addUser-here>);
 /*
  * Get a user, but not the password (FAIL).
  */
CALL getUser(-999);

/*
 * Update a user, but not the password (succeed)
 */
CALL putUser(<id-from-addUser-here>, 'Rick', 'rick@example.ca', True);
/*
 * Update a user, but not the password (FAIL)
 */
CALL putUser(-999, 'Rick', 'rick@example.ca', True);

/*
 * Delete a user (success) (add first here to get the id and doesn't wreck anything)
 */
CALL addUser('me', 'me@unb.ca','$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a', true);
CALL delUser(<id-from-addUser-here>);
/*
 * Delete a user (FAIL)
 */
CALL delUser(<id-from-addUser-here>);

/*
 * Verify user credentials (succeed)
 */
CALL verifyUser('you@unb.ca', '$2y$10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');

/*
 * Verify user credentials (FAIL)
 */
CALL verifyUser('you@example.ca', 'FAIL10$GvWXZUOc5Y1U12QJI5zj2uvyKPwshAc1h5teetXv2lsdI77P3q.5a');
