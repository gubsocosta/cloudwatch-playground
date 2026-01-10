<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/logs-test', function () {
    \Log::info('This is an info log message.');
    \Log::warning('This is a warning log message.');
    \Log::error('This is an error log message.');

    return response()->json(['message' => 'Logs have been written.']);
});
