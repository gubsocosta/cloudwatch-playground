FROM php:8.4-fpm-alpine

# Install system dependencies
RUN apk add --no-cache \
    curl \
    git \
    bash \
    openssl \
    nodejs \
    npm

# Set working directory
WORKDIR /var/www

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# Create a non-root user
RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser && \
    mkdir -p /home/appuser && \
    chown -R appuser:appuser /home/appuser

# Set ownership of working directory
RUN chown -R appuser:appuser /var/www

# Switch to non-root user
USER appuser

# Install Laravel installer globally
RUN composer global require laravel/installer

# Add Composer bin directory to PATH
ENV PATH="/home/appuser/.composer/vendor/bin:${PATH}"

# Set timezone
ENV TZ=America/Sao_Paulo

CMD ["php-fpm"]